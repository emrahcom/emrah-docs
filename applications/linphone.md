## Linphone

### installation

On `GNULinux`, download `AppImage` from [linphone.org](https://linphone.org/)
for `H264` support.

After download:

```bash
mkdir -p ~/bin
cp Linphone-4.4.1.AppImage ~/bin/
chmod 755 ~/bin/Linphone-4.4.1.AppImage
```

_Linphone-4.4.8.AppImage cannot allow H264 in my tests but
Linphone-4.4.1.AppImage works. Probably there is a new bug._

### clear old config

To reset `Linphone` config:

```bash
rm -rf ~/.config/linphone
rm -rf ~/.local/share/linphone
```

### H264 support

![Linphone H264 support](./images/linphone-h264.png)
