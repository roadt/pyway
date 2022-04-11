from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


# restirct to a particlar path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# create server
server = SimpleXMLRPCServer(('localhost', 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'ow'.
server.register_function(pow)


# register a fucntion under different name
def adder_function(x, y):
    return x+ y
server.register_function(adder_function, 'add')

# register an instance; all the methods of instance are
# published as XML-RPC methods (in this case, just 'div')
class MyFuncs:
    def div(self, x, y):
        return x//y
server.register_instance(MyFuncs())        


#RUn the server's main loop
server.serve_forever()


    
