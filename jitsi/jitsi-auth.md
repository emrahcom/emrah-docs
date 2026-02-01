# auth.html

The token authentication script for testing. Put it as
`/usr/share/jitsi-meet/static/auth.html`

```javascript
<script>
const host = "https://jitsi.emrah.com";
const qs = new URLSearchParams(window.location.search);
const state = JSON.parse(qs.get("state")) || {};
const room = state.room || "testroom";
const jwt = "eyJhb...";
const hashes = "#config.prejoinConfig.enabled=false" +
               "&config.deeplinking.disabled=false";
const url = `${host}/${room}?jwt=${jwt}${hashes}`;

window.location = url;
</script>
```
