from zeep import Client

#This example is taken from javaKing
# https://www.youtube.com/watch?v=JBYEQjg_znI

client = Client(wsdl="http://www.dneonline.com/calculator.asmx?wsdl")
print(client.service.Add(1,2))

