import time
import BaseHTTPServer
from urlparse import urlparse
from blockOps import getBlocks, generateNextBlock


class MyMiniHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Blockchain Example.</title></head>")
        s.wfile.write("<body><p>Processing:</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        if "blocks" in s.path:
            for st in getBlocks(s.server):
                s.wfile.write("<p>%s</p>" % st)
        elif "addBlock=" in s.path:
            index = s.path.find("addBlock=")
            #Text addblock has 9 characters!
            data = s.path[index+9:]
            block = generateNextBlock(s.server, data)
            s.server.addBlock(block)
            s.wfile.write("<p>Added new Block: %s</p>" % data)

        s.wfile.write("</body></html>")
