## virtualbox

Tested on `Debian Bullseye`.

#### installation

```bash
wget -O /tmp/vbox.key https://www.virtualbox.org/download/oracle_vbox_2016.asc
cat /tmp/vbox.key | gpg --dearmor > /usr/share/keyrings/oracle-vbox-keyring.gpg
```

_/etc/apt/sources.list.d/vbox.list_

```conf
deb [signed-by=/usr/share/keyrings/oracle-vbox-keyring.gpg] http://download.virtualbox.org/virtualbox/debian focal contrib non-free
```

```bash
apt-get update
apt-get install virtualbox-6.1 --install-recommends
```
