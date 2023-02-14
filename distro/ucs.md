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
- An IP from 172.18.18.0/24 on `br1` is OK

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

- Save the license key which is sent by e-mail
- Got to the web interface: `https://ucs.mydomain.corp`
- Login as `administrator`
- Go to `Welcome`
- Import a license
- Import from file

### Keycloak

Don't use `App Center`, it fails in this release. Install through `ssh`:

```bash
ssh -p 22 -l root ucs.mydomain.corp
univention-app install keycloak
```

`admin`'s password is in `/etc/keycloak.secret`.

- `Keycloak admin panel` in on `https://ucs-sso-ng.mydomain.corp/admin/`
- Updating `/etc/keycloak.secret` doesn't change the password.
- The `administrator` account cannot join the panel even the document says it
  should be.

Update `admin`'s password on

- `https://ucs-sso-ng.mydomain.corp/admin/`
- `Users` in `Master` realm
- `admin` -> `Credentials` -> `Password` -> `Reset password`
- Do not check `Temporary`

### Links

- https://docs.software-univention.de/keycloak-app/latest/installation.html
