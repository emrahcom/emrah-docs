# Bluetooth

Tested on `Debian 12 Bookworm` with `PipeWire`.

## packages

```bash
apt-get install bluez

systemctl status bluetooth.service
bluetoothd -v

rfkill
rfkill unblock bluetooth

bluetoothctl
  help
  power on
  scan on
  agent on
  pair <BLUETOOTH_ADDRESS>
  trust <BLUETOOTH_ADDRESS>
  info <BLUETOOTH_ADDRESS>
```
