## Android Debug Bridge

Tested on `Debian Bookworm`

#### installation

As `root`:

```bash
apt-get install adb
apt-get install ffmpeg wget git
apt-get install gcc pkg-config meson ninja-build
apt-get install libsdl2-2.0-0 libsdl2-dev libusb-1.0-0 libusb-1.0-0-dev \
  libavcodec-dev libavdevice-dev libavformat-dev libavutil-dev libswresample-dev
```

As `user`:

```bash
cd ~/git-repo
git clone https://github.com/Genymobile/scrcpy

cd scrcpy
bash install_release.sh
  # ctrl+c in sudo line
cp build-auto/app/scrcpy ~/bin/
```

As `root`:

```bash
mkdir -p /usr/local/share/scrcpy
cp /home/emrah/git-repo/scrcpy/build-auto/server/scrcpy-server \
  /usr/local/share/scrcpy/
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
- If this doesn't work, first disable `debugging` and allow it again.
- List attached devices

  ```bash
  adb devices
  ```

#### Screen mirroring

```bash
scrcpy
```

#### Stopping server

```bash
adb kill-server
```

#### Links

- https://github.com/Genymobile/scrcpy
- https://github.com/Genymobile/scrcpy/blob/master/doc/linux.md
