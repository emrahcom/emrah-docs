## Univention Corporate Server (UCS)

Tested on `Virt-Manager` on `Debian 11 Bullseye`

### Download

[UCS Download](https://www.univention.com/downloads/download-ucs/)

- Fill the form
- Download `KVM` version

or

```bash
wget -O ~/downloads/UCS-KVM-Image-5.0-3.qcow2 \
    https://updates.software-univention.de/download/images/UCS-KVM-Image.qcow2
```

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
- License
  - Save the license key which is sent by e-mail
  - Got to the web interface: https://ucs.mydomain.corp
  - Login as `administrator`
  - Go to `Welcome`
  - Import a license
  - Import from file
