import time
import BaseHTTPServer
from urlparse import urlparse


class MyMiniServer(BaseHTTPServer.HTTPServer):
    def __init__(self, *args, **kwargs):
        # Because HTTPServer is an old-style class, super() can't be used.
        BaseHTTPServer.HTTPServer.__init__(self, *args, **kwargs)
        self.blockchain = []

    def addBlock(self, b):
        self.blockchain.append(b)
