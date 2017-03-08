#!/usr/bin/env python
import hashlib
import time
import BaseHTTPServer
from block import Block
from urlparse import urlparse
from minihandler import MyMiniHandler
from miniserver import MyMiniServer


if __name__ == "__main__":
    HOST_NAME = '127.0.0.1' # !!!REMEMBER TO CHANGE THIS!!!
    PORT_NUMBER = 8000 # Maybe set this to 9000.
    server_class = BaseHTTPServer.HTTPServer
    server_class = MyMiniServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyMiniHandler)
    print time.asctime(), "Starting server time: - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server stoped: - %s:%s" % (HOST_NAME, PORT_NUMBER)
