"""Serve the site locally at /Aarav-Portfolio/ to match the GitHub Pages project URL.

Usage: python tools/serve_local.py [port]
Then open http://localhost:8000/Aarav-Portfolio/
"""
import http.server
import pathlib
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
PREFIX = "/Aarav-Portfolio"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_head(self):
        path = urllib.parse.urlsplit(self.path).path
        if path == PREFIX:
            self.send_response(301)
            self.send_header("Location", PREFIX + "/")
            self.end_headers()
            return None
        if not path.startswith(PREFIX + "/"):
            return self._not_found()
        self.path = self.path[len(PREFIX):]
        target = pathlib.Path(self.translate_path(self.path))
        if not target.exists():
            return self._not_found()
        return super().send_head()

    def _not_found(self):
        # Mirrors GitHub Pages, which serves 404.html for any missing path.
        body = (ROOT / "404.html").read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        return None


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"Serving at http://localhost:{port}{PREFIX}/  (Ctrl+C to stop)")
    http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
