import socket as socket

localIP = '127.0.0.1'
localPort = 20001
bufferSize = 1024

msg = "Hello Client" 
dataSize = str.encode(msg)

udpServer = socket.socket(family=socket.AF_INET , type = socket.SOCK_DGRAM)

udpServer.bind((localIP,localPort))

print("udp server up and listening")


while(True):
    bytesAddressPair = udpServer.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address =  bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    udpServer.sendto(dataSize , address)

