## pjsua

### pjsua.config

```config
--video
--no-color
--log-level=5
--app-log-level=5
--auto-update-nat 0
--disable-stun
--no-tcp
--dis-codec GSM
--dis-codec H263
--dis-codec iLBC
--dis-codec G722
--dis-codec speex
--dis-codec pcmu
--dis-codec pcma
--dis-codec opus
--add-codec pcmu
--add-codec pcma
--add-codec speex
--add-codec G722
--add-codec opus
--no-vad
--ec-tail 0
--quality 10
--max-calls=1
--auto-keyframe=30
--no-stderr
--log-file=/home/dodo/pjsua/pjsua.log
```

### Run as server

```bash
pjsua --config-file=./pjsua.config --auto-answer=200
```

### Run as client

```bash
pjsua --config-file=./pjsua.config "sip:dodo@172.17.17.33"
```

### References

- [pjsua](https://www.pjsip.org/pjsua.htm)
