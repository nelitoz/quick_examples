from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x+y

server = SimpleXMLRPCServer(("localhost",6789))
server.register_function(add, "add")
server.serve_forever()

