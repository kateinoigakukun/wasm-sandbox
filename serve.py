#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import mimetypes

PORT = 8081

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

Handler.extensions_map['.wasm']='application/wasm'
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
