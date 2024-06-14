// -----------------------------------------------------------------------------
// Usage:
//   deno run --allow-net wss-server.ts
// -----------------------------------------------------------------------------
import { serve } from "https://deno.land/std/http/server.ts";

const HOSTNAME = "0.0.0.0";
const PORT = 8000;

// -----------------------------------------------------------------------------
function onOpen(e: Event) {
  console.log("onOpen");
  console.log(e);
}

// -----------------------------------------------------------------------------
function onMessage(ws: WebSocket, e: MessageEvent) {
  console.log("onMessage");
  console.log(ws);
  console.log(e.data);
  ws.send("ok");
}

// -----------------------------------------------------------------------------
function onClose(e: CloseEvent) {
  console.log("onClose");
  console.log(e);
}

// -----------------------------------------------------------------------------
function onError(e: Event | ErrorEvent) {
  console.log("onError");
  console.log(e);
}

// -----------------------------------------------------------------------------
function handler(req: Request): Response {
  if (req.headers.get("upgrade") != "websocket") {
    console.log("no upgrade request, rejected");
    return new Response(null, { status: 501 });
  }

  const { socket, response } = Deno.upgradeWebSocket(req);
  socket.onopen = onOpen;
  socket.onmessage = (e) => onMessage(socket, e);
  socket.onclose = onClose;
  socket.onerror = onError;

  return response;
}

// -----------------------------------------------------------------------------
function main() {
  console.log("Waiting for client ...");

  serve(handler, {
    hostname: HOSTNAME,
    port: PORT,
  });
}

// -----------------------------------------------------------------------------
main();
