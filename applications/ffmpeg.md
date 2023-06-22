## ffmpeg

### pulse sources

```bash
pactl list short sources
```

### record audio from source

```bash
ffmpeg -f pulse -i default audio-$(date +'%Y%m%d%H%M%S').mp3
ffmpeg -f pulse -i <SOURCE_ID> audio-$(date +'%Y%m%d%H%M%S').mp3
```
