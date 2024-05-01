"""
This script is tested on Debian 12 Bookworm.
Required packages: python3 python3-requests

Enable python3 in /etc/freeswitch/autoload_configs/modules.conf.xml

  <load module="mod_python3"/>

Put this file into /usr/local/lib/python3.11/dist-packages/nordeck/

Create /usr/local/lib/python3.11/dist-packages/nordeck/__init__.py
  touch /usr/local/lib/python3.11/dist-packages/nordeck/__init__.py

Add /etc/freeswitch/dialplan/public/98_public_sipjibri_dialplan.xml

Add /etc/freeswitch/dialplan/default/99_default_sipjibri_dialplan.xml

Add the component-selector URL in /etc/freeswitch/vars.xml
Add component_verify_certificate if its certificate is self-signed

  <X-PRE-PROCESS cmd="set" data="component_selector_url=https://domain/path"/>
  <X-PRE-PROCESS cmd="set" data="component_verify_certificate=false"/>

Add "sipjibri-users" folder in /etc/freeswitch/directory/default.xml

  <groups>
    <group name="default">
      <users>
        <X-PRE-PROCESS cmd="include" data="default/*.xml"/>
        <X-PRE-PROCESS cmd="include" data="/tmp/sipjibri/*.xml"/>
      </users>
    </group>
  </groups>

Restart FreeSwitch
  systemctl restart freeswitch.service
"""

from datetime import datetime, timedelta
from glob import glob
from os import makedirs, remove
from os.path import getmtime
from random import randint
from time import time
import json
from requests import post
import freeswitch

EXTENSION_EXPIRE_MINUTES = 60
USER_DIR = "/tmp/sipjibri"
USER_TPL = """
<include>
  <user id="{sipUser}">
    <params>
      <param name="password" value="{sipPass}"/>
    </params>
    <variables>
      <variable name="toll_allow" value="local"/>
      <variable name="user_context" value="default"/>
    </variables>
  </user>
</include>
"""

# pylint: disable=bare-except

# ------------------------------------------------------------------------------
def create_extension(api, session, sip_domain, sip_user, sip_pass):
    """
    Create a temporary SIP extension only for this session.
    """

    try:
        # Create the extension config file
        makedirs(USER_DIR, exist_ok=True)
        xml = USER_TPL.format(
            sipDomain=sip_domain,
            sipUser=sip_user,
            sipPass=sip_pass,
        )
        path = f"{USER_DIR}/sipjibri_{sip_user}.xml"
        with open(path, "w", encoding="utf-8") as file:
            file.write(xml)

        # Reload config to activate the new extension
        reply = api.executeString("reloadxml")
        freeswitch.consoleLog("info", f"reload result: {reply}\n")
        session.sleep(500)

        return True
    except:
        pass

    return False

# ------------------------------------------------------------------------------
def request_meeting_data(pin):
    """
    Get the meeting data from API service by using PIN.
    """

    # Dont continue if there is no pin
    if pin == "":
        return {}

    # There will be some api request here which gets the meeting details from
    # Booking Portal by sending the pin number.
    if pin == "123456":
        return {
            "host": "https://jitsi.nordeck.corp",
            "room": "myroom",
        }

    return {}

# ------------------------------------------------------------------------------
def request_sipjibri(sip_domain, sip_user, sip_pass, meeting):
    """
    Send a request to component-selector for a SIP-Jibri instance
    """

    try:
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "callParams": {
                "callUrlInfo": {
                    "baseUrl": meeting.get("host"),
                    "callName": meeting.get("room")
                }
            },
            "componentParams": {
                "type": "SIP-JIBRI",
                "region": "default-region",
                "environment": "default-env"
            },
            "metadata": {
                "sipClientParams": {
                    "userName": f"{sip_user}@{sip_domain}",
                    "password": f"{sip_pass}",
                    "contact": f"<sip:{sip_user}@{sip_domain}>",
                    "sipAddress": "sip:jibri@127.0.0.1",
                    "displayName": "Cisco",
                    "autoAnswer": True,
                    "autoAnswerTimer": 30
                }
            }
        }

        api = freeswitch.API()
        url = api.executeString("global_getvar component_selector_url")
        if not url:
            return False
        freeswitch.consoleLog("info", f"component_selector_url: {url}")

        verify = api.executeString("global_getvar component_verify_certificate")
        if not verify:
            verify = True
        elif verify.lower() == "false":
            verify = False
        else:
            verify = True
        freeswitch.consoleLog("info", f"component_verify_certificate: {verify}")

        json_data = json.dumps(data)
        freeswitch.consoleLog("info", f"post data: {json_data}")
        res= post(
            url,
            headers=headers,
            data=json_data,
            timeout=10,
            verify=verify,
        )
        json_res = res.json()
        freeswitch.consoleLog("info", f"post result: {json_res}")

        if json_res.get("componentKey"):
            return True
    except:
        pass

    return False

# ------------------------------------------------------------------------------
def get_meeting(session):
    """
    Ask the caller for PIN and get the meeting data from API service.
    """

    try:
        # Ask for PIN
        session.streamFile("conference/conf-pin.wav")

        i = 1
        while True:
            # get PIN
            pin = session.getDigits(6, "#", 8000)
            freeswitch.consoleLog("info", f"PIN NUMBER {i}: {pin}")

            # Completed if there is a valid reply from API service for this PIN
            meeting= request_meeting_data(pin)
            if meeting:
                return meeting

            # Dont continue if there are many failed attempts.
            i += 1
            if i > 3:
                break

            # Ask again after the failed attempt.
            if pin:
                session.streamFile("conference/conf-bad-pin.wav")
            else:
                session.streamFile("conference/conf-pin.wav")
    except:
        pass

    return {}

# ------------------------------------------------------------------------------
def remove_expired_extensions():
    """
    Remove expired SIP-Jibri extensions.
    """

    try:
        expire_at = datetime.now() - timedelta(minutes=EXTENSION_EXPIRE_MINUTES)

        # Trace SIP-Jibri extension folder and remove expired config files.
        for file in glob(f"{USER_DIR}/sipjibri_*.xml"):
            if getmtime(file) < expire_at.timestamp():
                remove(file)
    except:
        pass

# ------------------------------------------------------------------------------
def invite_sipjibri(session, meeting):
    """
     - Create a temporary SIP extension only for this session
     - Invite SIP-Jibri by using this extension
    """

    try:
        api = freeswitch.API()

        # Generate extension data
        sip_domain = api.executeString("global_getvar domain")
        sip_user = str(int(time() * 1000))[-9:]
        sip_pass = randint(10**8, 10**9 - 1)

        # Create the extension
        if not create_extension(api, session, sip_domain, sip_user, sip_pass):
            return None

        # Send a request to component-selector for a SIP-Jibri instance
        okay = request_sipjibri(sip_domain, sip_user, sip_pass, meeting)
        if not okay:
            return None

        return sip_user
    except:
        return None

# ------------------------------------------------------------------------------
def handler(session, _args):
    """
    Call handler. This is the main entrypoint.
    """

    try:
        freeswitch.consoleLog("info", "sipjibri handler\n")

        # Answer the call
        session.answer()
        session.sleep(2000)

        # Get the meeting info. Cancel the request if no meeting info.
        # The conference PIN number will be asked during this process.
        meeting = get_meeting(session)
        if not meeting:
            session.hangup()
            return

        # Remove expired extensions
        remove_expired_extensions()

        # Invite SIP-Jibri to the meeting
        sip_jibri_extension = invite_sipjibri(session, meeting)
        freeswitch.consoleLog(
            "info",
            f"SIP-Jibri extension: {sip_jibri_extension}\n"
        )
        if not sip_jibri_extension:
            session.hangup()
            return

        # Request is accepted
        freeswitch.consoleLog("info", "the conference request is accepted\n")
        session.streamFile("conference/conf-conference_will_start_shortly.wav")
        session.sleep(3000)

        # Transfer the call to SIP-Jibri extension
        session.transfer(sip_jibri_extension, "XML", "default")
    except:
        pass
