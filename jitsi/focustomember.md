# Focus To Member

```javascript
<script>
function setFocusedMember() {
  let targetId = '';

  try {
    const plist= APP.store.getState()['features/base/participants'].remote;
    plist.forEach((p) => {
      if (p.role !== 'moderator') {
        targetId = p.id;
      }
    });

    if (targetId !== APP.UI.getLargeVideoID()) {
      APP.store.dispatch({
        type: 'PIN_PARTICIPANT',
        participant: {
          id: targetId
        }
      });

      //APP.UI.updateLargeVideo(p.id);

      //APP.store.dispatch({
      //  type: 'SELECT_LARGE_VIDEO_PARTICIPANT',
      //  participantId: p.id
      //});
    }
  } catch(e) {
    // nothing to do
  } finally {
    setTimeout(function() {setFocusedMember();}, 1000);
  }
}

function focusToMember() {
  try {
    var isRecorder = APP.store.getState()['features/base/config'].iAmRecorder;
    if (!isRecorder) return false;

    APP.store.dispatch({type: 'SET_TILE_VIEW', enabled: false});
    APP.store.dispatch({type: 'SET_FILMSTRIP_VISIBLE', visible: false});

    setTimeout(function() {setFocusedMember();}, 1000);
  } catch(e) {
    setTimeout(function() {focusToMember();}, 1000);
  }
}

focusToMember();
</script>
```
