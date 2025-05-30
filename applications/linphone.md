## Linphone

### installation

On `GNULinux`, download `AppImage` from
[Linphone](https://download.linphone.org/releases/linux/app/) for `H.264`
support.

After download as `root`:

```bash
cp Linphone-5.2.2.AppImage /usr/local/bin/
chmod 755 /usr/local/bin/Linphone-5.2.2.AppImage
```

As `user`:

```bash
mkdir -p ~/bin
ln -sf /usr/local/bin/Linphone-5.2.2.AppImage ~/bin/linphone
```

### clear old config

To reset `Linphone` config:

```bash
rm -rf ~/.config/linphone
rm -rf ~/.local/share/linphone
```

### after installation

- Add account
  - Use `TCP`.
- Set `Registration duration` as 90 sec (see also
  [FreeSwitch](/services/freeswitch.md) notes)
- Set `audio` devices
  - Disable `G729`. It breaks `Jigasi` communication.
- Set `video` to `720p`
- Set `auto answer` to `2000ms`
- Set `auto answer (with video)`
- Add `H.264` support

### H.264 support

![Linphone H.264 support](/images/linphone-h264.png)
