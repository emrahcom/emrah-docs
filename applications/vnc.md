# VNC

## Remote

```bash
apt-get install x11vnc xdotool
```

Run as user preferebly in `tmux`:

```bash
x11vnc -display :0 -rfbport 5900 -nolookup -once -loop -usepw -shared -noxdamage -nodpms
```

## Local

```bash
apt-get install xtightvncviewer
```

Run as user:

```bash
vncviewer IP:port
```

Send keys:

```bash
ssh -Y IP
DISPLAY=:0 xdotool key Super+Shift+c
```
