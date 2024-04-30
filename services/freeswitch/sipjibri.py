# ------------------------------------------------------------------------------
# This script is tested on Debian 12 Bookworm.
#
# Put this file into /usr/local/lib/python3.11/dist-packages/nordeck/
#
# Create /usr/local/lib/python3.11/dist-packages/nordeck/__init__.py
#   touch /usr/local/lib/python3.11/dist-packages/nordeck/__init__.py
#
# Add /etc/freeswitch/dialplan/public/98_public_sipjibri_dialplan.xml
#
# Add /etc/freeswitch/dialplan/default/99_default_sipjibri_dialplan.xml
#
# Add "sipjibri-users" folder in /etc/freeswitch/directory/default.xml
#
#   <groups>
#     <group name="default">
#       <users>
#         <X-PRE-PROCESS cmd="include" data="default/*.xml"/>
#         <X-PRE-PROCESS cmd="include" data="/tmp/sipjibri-users/*.xml"/>
#       </users>
#     </group>
#   </groups>
# ------------------------------------------------------------------------------
import freeswitch
from datetime import datetime, timedelta
from glob import glob
from os import makedirs, remove
from os.path import getmtime
from random import randint
from time import time

EXPIRE_MINUTES = 60
USER_DIR = "/tmp/sipjibri-users"
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

# ------------------------------------------------------------------------------
def requestMeetingData(pin):
  try:
    if pin == "": raise

    # there will be some api request here which gets the meeting details from
    # Booking Portal by sending the pin number.
    if pin == "123456":
      return {
        "name": "myroom"
      }
  except Exception as e:
    return {}

# ------------------------------------------------------------------------------
def getMeeting(session):
  try:
    session.streamFile(f"conference/conf-pin.wav")

    i = 1
    while True:
      pin = session.getDigits(6, "#", 8000)
      freeswitch.consoleLog("info", f"PIN NUMBER {i}: {pin}")

      meeting= requestMeetingData(pin)
      if meeting: return meeting

      i += 1
      if i > 3: break

      if pin:
        session.streamFile(f"conference/conf-bad-pin.wav")
      else:
        session.streamFile(f"conference/conf-pin.wav")
  except Exception as e:
    pass

  return {}

# ------------------------------------------------------------------------------
# Remove expired SIP-Jibri extention.
# ------------------------------------------------------------------------------
def removeOldExtensions():
  try:
    expireAt = datetime.now() - timedelta(minutes=EXPIRE_MINUTES)

    for ext in glob(f"{USER_DIR}/sipjibri_*.xml"):
      if getmtime(ext) < expireAt.timestamp():
        remove(ext)
  except Exception as e:
    pass

# ------------------------------------------------------------------------------
# Create a temporary SIP extension only for this session and use it for
# SIP-Jibri
# ------------------------------------------------------------------------------
def inviteSipJibri(session, meeting):
  try:
    api = freeswitch.API()

    sipDomain = api.executeString("global_getvar domain")
    sipUser = str(int(time() * 1000))[-9:]
    sipPass = randint(10**8, 10**9 - 1)

    makedirs(USER_DIR, exist_ok=True)
    xml = USER_TPL.format(sipDomain=sipDomain, sipUser=sipUser, sipPass=sipPass)
    with open(f"{USER_DIR}/sipjibri_{sipUser}.xml", "w") as f:
      f.write(xml)

    reply = api.executeString("reloadxml")
    freeswitch.consoleLog("info", f"reload reply: {reply}\n")
    session.sleep(500)

    return sipUser
  except Exception as e:
    return None

# ------------------------------------------------------------------------------
def handler(session, args):
  try:
    freeswitch.consoleLog("info", "cisco handler\n")

    session.answer()
    session.sleep(2000)

    meeting = getMeeting(session)
    if not meeting:
      session.hangup()
      return

    freeswitch.consoleLog("info", "the conference request is accepted\n")
    session.streamFile(f"conference/conf-conference_will_start_shortly.wav")
    session.sleep(500)

    removeOldExtensions()
    sipJibriExtention = inviteSipJibri(session, meeting)
    freeswitch.consoleLog("info", "SIP-Jibri extention: {sipJibriExtention}\n")
    if not sipJibriExtention:
      session.hangup()
      return

    session.transfer(sipJibriExtention, "XML", "default");
  except Exception as e:
    pass

# ------------------------------------------------------------------------------
def fsapi(session, stream, env, args):
  freeswitch.consoleLog("info", "cisco fsapi\n")
