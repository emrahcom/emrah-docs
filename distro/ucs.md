## Univention Corporate Server (UCS)

Tested on `Virt-Manager` on `Debian 11 Bullseye`.

### Download

[UCS Download](https://www.univention.com/downloads/download-ucs/)

- Fill the form
- Download `KVM` version

or

```bash
wget -O ~/downloads/UCS-KVM-Image-5.0-3.qcow2 \
    https://updates.software-univention.de/download/images/UCS-KVM-Image.qcow2
```

### FQDNs and IPs

- `ucs.mydomain.corp`
- `ucs-sso.mydomain.corp`
- `ucs-sso-ng.mydomain.corp`

- `172.17.0.0/16` is already reserved for `Docker` containers. Don't use an IP
  from this block as the server IP.
- `172.16.1.0/24` started to be used by `UCS` after `Keycloak` installation.
  Don't use an IP from this block as the server IP.
- An IP from `172.18.18.0/24` on `br1` is OK

### Installation

```bash
cp UCS-KVM-Image-5.0-3.qcow2 /var/lib/libvirt/images/ucs-20230213.qcow2
```

`Virt-Manager`

- Create a new machine
- Import existing disk image
- Choose `/var/lib/libvirt/images/ucs-20230213.qcow2`
- Choose `Debian 10` as OS
- Hardware
  - 8192 MB RAM
  - 2 CPU cores
- Network
  - bridge: `br1`
- Installer
  - English
  - Localization (default)
  - Network (static)
    - Address: `172.18.18.20`
    - Netmask: `255.255.255.0`
    - Gateway: `172.18.18.1`
    - DNS: `172.18.18.1`
  - Create a new UCS domain
  - Organization
    - `emrah`
    - a valid e-mail
    - pass
  - Host
    - FQDN: `ucs.mydomain.corp`
    - LDAP: `dc=mydomain,dc=corp`

### License

- Save the license key which is sent by an e-mail.
- Go to the web interface: `https://ucs.mydomain.corp`
- Login as `administrator`
- Go to `Welcome`
- Import a license
- Import from file

### Keycloak

Installing `Keycloak` through the web panel fails sometimes. No idea why...

- `https://ucs.mydomain.corp`
- `App Center`
- `Keycloak`
- `Install`
- No need to change defaults
- `Start Installation`

or through `ssh`:

```bash
ssh -p 22 -l root ucs.mydomain.corp
univention-app install keycloak
```

Run `50keycloak`:

- `Domain` -> `Domain Join`
- Select `50keycloak` -> `Execute`
- `Run join scripts`
- `Restart` (_UMC server components_)

`admin`'s password is in `/etc/keycloak.secret`. `Keycloak Admin Console` is on
`https://ucs-sso-ng.mydomain.corp/admin/`. It is possible to use `administrator`
account while connecting to `Keycloak Admin Console`.

**Warning:** _Create a shapshot after this step_

### SSO

- `https://ucs.mydomain.corp`
- `System` -> `Univention Configuration Registry` -> `umc/saml/idp-server`
  \
  `https://ucs-sso-ng.mydomain.corp/realms/ucs/protocol/saml/descriptor`
- `Domain` -> `Portal` -> `login-saml` -> `Activated` -> `Save`
- `System` -> `System services` -> `slapd` -> `restart`

### Users

Add users through `UCS Portal`. Don't add directly through `Keycloak`.

- `Domain` -> `Mail` -> `Add`
- `mydomain.corp` -> `Create mail object`

- `Users` -> `Add`
- Set `email` after adding

### Links

- https://docs.software-univention.de/keycloak-app/latest/installation.html
- https://www.keycloak.org/docs/19.0.3/server_admin/#_client-saml-configuration
