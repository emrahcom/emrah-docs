## bluetoothctl

It is available by default in most cases. In Debian Trixie:

```bash
dpkg -l '*blue*' | egrep '^ii'

ii  blueman                     2.3.5-2+b1
ii  bluez                       5.66-1+deb12u2
ii  bluez-obexd                 5.66-1+deb12u2
ii  libbluetooth3:amd64         5.66-1+deb12u2
ii  libspa-0.2-bluetooth:amd64  0.3.65-3+deb12u1
```

#### Commands

Open `bluetoothctl` shell:

```bash
# List all commands
help

# Devices
devices
devices [Paired/Bonded/Trusted/Connected]

# Connect (use the tab key to complete MAC)
connect MAC_ADDRESS

# Trust
trust MAC_ADDRESS

# Pair
pair MAC_ADDRESS
```
