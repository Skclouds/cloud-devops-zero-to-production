import json
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

config_path = Path.home() / "devops-lab/scenario-02/config.json"

with open(config_path) as file:
    config = json.load(file)

port = config["port"]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Application is healthy")

server = HTTPServer(("127.0.0.1", port), Handler)

print(f"Application running on port {port}", flush=True)
server.serve_forever()
