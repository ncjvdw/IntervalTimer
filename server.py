import http.server
import ssl

server_address = ("0.0.0.0", 8000)

httpd = http.server.HTTPServer(
    server_address,
    http.server.SimpleHTTPRequestHandler
)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    "localhost+3.pem",
    "localhost+3-key.pem"
)

httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True
)

httpd.serve_forever()