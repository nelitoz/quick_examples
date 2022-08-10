import xmlrpc.client

proxy=xmlrpc.client.ServerProxy("http://localhost:6789/")
x=50
y=50

result = proxy.add(x,y)
print(f"Result is: {result}")

