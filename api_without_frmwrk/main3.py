# from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
#
# import http.server
# import socketserver
#
#
# class GetHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == "/":
#             self.path = "index.html"
#             return SimpleHTTPRequestHandler(self)
#
#
# Handler = GetHandler
#
# # httpd = HTTPServer(("localhost", 8080), Handler)
# # httpd.serve_forever()
# myserver = socketserver.TCPServer(("localhost", 8080), Handler)
# myserver.serve_forever()
