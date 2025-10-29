# ffmpeg

### pulse sources

```bash
pactl list short sources
```

### record audio from source

```bash
ffmpeg -f pulse -i default audio-$(date +'%Y%m%d%H%M%S').mp3
ffmpeg -f pulse -i <SOURCE_ID> audio-$(date +'%Y%m%d%H%M%S').mp3
```

### amerge

```bash
ffmpeg -f pulse -i default -f pulse -i 54 \
  -filter_complex "[0:0][1:0] amerge=inputs=2" \
  -c:a aac  audio-$(date +'%Y%m%d%H%M%S').mkv
```
