#!/usr/bin/env python3

from xmlrpc.server import *
import random, uuid

class Box:
    def bool(self):
        return random.randint(0,1) > 0 and True or False
        
    def list(self):
        return []

    def dict(self):
        return {}

    def int(self):
        return random.randint(1, 100)

    def float(self):
        return random.random()

    def str(self):
        return uuid.uuid1().hex


server = SimpleXMLRPCServer(('localhost', 8000))
server.register_introspection_functions()        
server.register_instance(Box())
server.serve_forever()