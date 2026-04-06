const MAX_RECORDING_DURATION_MS = 2 * 3600 * 1000;
const PREFERRED_MEDIA_TYPE = "video/webm;codecs=vp8,opus";
const VIDEO_BIT_RATE = 2500000;

// -----------------------------------------------------------------------------
async function getLocalStream() {
  const localStream = await navigator.mediaDevices.getUserMedia({
    audio: {
      autoGainControl: true,
      echoCancellation: true,
      noiseSuppression: true,
    },
  });

  return localStream;
}

// -----------------------------------------------------------------------------
async function getRemoteStream() {
  const remoteStream = await navigator.mediaDevices.getDisplayMedia({
    audio: {
      autoGainControl: false,
      echoCancellation: false,
      noiseSuppression: false,
    },
    video: {
      cursor: "always",
      displaySurface: "browser",
      frameRate: {
        ideal: 30,
        max: 60,
      },
    },
    selfBrowserSurface: "include",
    surfaceSwitching: "include",
  });

  return remoteStream;
}

// -----------------------------------------------------------------------------
function getMixedStream(audioContext, localStream, remoteStream) {
  const dest = audioContext.createMediaStreamDestination();

  const micSource = audioContext.createMediaStreamSource(localStream);
  micSource.connect(dest);

  if (remoteStream.getAudioTracks().length > 0) {
    const systemSource = audioContext.createMediaStreamSource(remoteStream);
    systemSource.connect(dest);
  }

  const mixedStream = new MediaStream([
    remoteStream.getVideoTracks()[0],
    dest.stream.getAudioTracks()[0],
  ]);

  return mixedStream;
}

// -----------------------------------------------------------------------------
function getRecorder(localStream, remoteStream, mixedStream, audioContext) {
  const options = {
    audioBitrateMode: "constant",
    mimeType: MediaRecorder.isTypeSupported(PREFERRED_MEDIA_TYPE)
      ? PREFERRED_MEDIA_TYPE
      : "video/webm",
    videoBitsPerSecond: VIDEO_BIT_RATE,
  };

  const recorder = new MediaRecorder(mixedStream, options);
  const chunks = [];

  remoteStream.getVideoTracks()[0].onended = () => {
    if (recorder.state === "recording") recorder.stop();
  };

  recorder.ondataavailable = (e) => {
    if (e.data.size > 0) chunks.push(e.data);
  };

  recorder.onstop = () => {
    const blob = new Blob(chunks, { type: recorder.mimeType });
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = `recording-${Date.now()}.webm`;
    a.click();

    setTimeout(() => {
      URL.revokeObjectURL(url);
    }, 1000);

    [remoteStream, localStream].forEach((s) =>
      s.getTracks().forEach((t) => t.stop())
    );

    if (audioContext && audioContext.state !== "closed") audioContext.close();
  };

  return recorder;
}

// -----------------------------------------------------------------------------
function preventClosure(e) {
  e.preventDefault();
  e.returnValue = "";
}

// -----------------------------------------------------------------------------
async function record() {
  let audioContext;
  let localStream;
  let remoteStream;

  try {
    remoteStream = await getRemoteStream();
    localStream = await getLocalStream();

    audioContext = new AudioContext();
    const mixedStream = getMixedStream(
      audioContext,
      localStream,
      remoteStream,
    );

    const recorder = getRecorder(
      localStream,
      remoteStream,
      mixedStream,
      audioContext,
    );

    recorder.start();

    globalThis.addEventListener("beforeunload", preventClosure);
    recorder.addEventListener("stop", () => {
      globalThis.removeEventListener("beforeunload", preventClosure);
    }, { once: true });

    setTimeout(() => {
      if (recorder.state === "recording") recorder.stop();
    }, MAX_RECORDING_DURATION_MS);
  } catch {
    if (localStream) localStream.getTracks().forEach((t) => t.stop());
    if (remoteStream) remoteStream.getTracks().forEach((t) => t.stop());
    if (audioContext) audioContext.close();
  }
}
