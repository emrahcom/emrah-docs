## Linphone

### installation

On `GNULinux`, download `AppImage` from
[Linphone](https://download.linphone.org/releases/linux/app/) for `H.264`
support.

After download:

```bash
cp Linphone-5.0.10.AppImage /usr/local/bin/
chmod 755 /usr/local/bin/Linphone-5.0.10.AppImage

mkdir -p ~/bin
ln -s /usr/local/bin/Linphone-5.0.10.AppImage ~/bin/linphone
```

### clear old config

To reset `Linphone` config:

```bash
rm -rf ~/.config/linphone
rm -rf ~/.local/share/linphone
```

### after installation

- Add account
- Set `audio` devices
- Set `video` to `720p`
- Set `auto answer` to `2000ms`
- Set `auto answer (with video)`
- Add `H.264` support

### H.264 support

![Linphone H.264 support](/images/linphone-h264.png)
