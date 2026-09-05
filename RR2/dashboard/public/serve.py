#!/usr/bin/env python
"""Serve the RoadRakshak control room.

  python3 serve.py                     # http://localhost:8090
  python3 serve.py --host 0.0.0.0      # reachable from other machines
  python3 serve.py --no-browser        # headless

Standard library only: no pip install, no framework, no internet.
"""
from __future__ import annotations

import sys

if sys.version_info < (3, 8):                     # a clear message beats a
    sys.exit(                                     # confusing SyntaxError
        "RoadRakshak needs Python 3.8 or newer.\n"
        f"You are running {sys.version.split()[0]} from {sys.executable}.\n"
        "Try:  python3 serve.py")

import argparse
import http.server
import json
import socketserver
import threading
import webbrowser
from functools import partial
from pathlib import Path

HERE = Path(__file__).resolve().parent


IMG_EXT = {".jpg", ".jpeg", ".png", ".webp"}


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        # Listing the folder live means renaming a file to a new number plate
        # takes effect on reload — no rebuild, no editing JSON.
        if self.path.split("?")[0] == "/api/violations":
            d = HERE / "violation"
            names = sorted(p.name for p in d.iterdir()
                           if p.is_file() and p.suffix.lower() in IMG_EXT) \
                if d.is_dir() else []
            body = json.dumps({"files": names}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def end_headers(self):
        # video scrubbing needs range requests; keep media uncached while iterating
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8090)
    ap.add_argument("--host", default="127.0.0.1",
                    help="0.0.0.0 makes the dashboard reachable from other "
                         "machines on the network. There is no authentication, "
                         "so use it only on a trusted network.")
    ap.add_argument("--no-browser", action="store_true")
    a = ap.parse_args()

    h = partial(Handler, directory=str(HERE))
    socketserver.TCPServer.allow_reuse_address = True

    shown = "localhost" if a.host in ("127.0.0.1", "localhost") else a.host
    print(f"  RoadRakshak control room -> http://{shown}:{a.port}")
    if a.host == "0.0.0.0":
        print("  bound to all interfaces - no authentication, trusted networks only")
    print("  Ctrl-C to stop")

    if not a.no_browser:
        # On a headless Linux box there is no browser and no DISPLAY; opening
        # one must never take the server down with it.
        def _open():
            try:
                webbrowser.open(f"http://localhost:{a.port}")
            except Exception:
                pass
        threading.Timer(0.9, _open).start()

    try:
        srv = socketserver.TCPServer((a.host, a.port), h)
    except OSError as e:
        print(f"\n  cannot bind {a.host}:{a.port} - {e}")
        print(f"  another process may hold the port. Try:  "
              f"python3 serve.py --port {a.port + 1}")
        return 1
    with srv:
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\n  stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
