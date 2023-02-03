## Android Debug Bridge

Tested on `Debian Bullseye`

#### installation

Add `backports` into `/etc/apt/sources.list`

```
deb https://deb.debian.org/debian bullseye-backports main
```

```bash
apt-get update
apt-get install adb
apt-get install scrcpy/bullseye-backports
```

#### Enabling the debug mode on phone

- `Settings`
- `About phone`
- `Software information`
- `Build number`
- Click 7 times
- Enter `password` then the developer mode will be turned on

#### Disabling the debug mode on phone

- `Settings`
- `Developer options`
- `Off`

#### Enabling USB debugging

- `Settings`
- `Developer options`
- Enable `USB debugging`

#### Attaching the phone

- start the `adb` server. Use the normal user account

  ```bash
  adb start-server
  ```

- Attach the phone using a USB cable
- `Allow USB debugging` message on the phone, allow it
- List attached devices

  ```bash
  adb devices
  ```

#### Screen mirroring

```bash
scrcpy
```
