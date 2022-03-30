
from xmlrpc.server import *

class MyFuncs:
    def __init__(self):
        import sys
        self.sys = sys
        
    def _listMethods(self):
        return list_public_methods(self) + \
                ['sys.' + method for method in list_public_methods(self.sys)]
        

    def pow(self, x, y):
        return pow(x, y)

    def add(self, x, y):
        return x + y

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_introspection_functions()        
server.register_instance(MyFuncs())
server.serve_forever()