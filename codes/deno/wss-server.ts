import { serve } from "https://deno.land/std/http/server.ts";

const HOSTNAME = "0.0.0.0";
const PORT = 8000;

// -----------------------------------------------------------------------------
function onMessage(e: MessageEvent) {
  console.log(e.data);
}

// -----------------------------------------------------------------------------
function handler(req: Request): Response {
  if (req.headers.get("upgrade") != "websocket") {
    return new Response(null, { status: 501 });
  }

  const { socket, response } = Deno.upgradeWebSocket(req);
  socket.onmessage = onMessage;

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
