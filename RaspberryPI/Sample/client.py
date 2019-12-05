import socket

msg = 'Hello UDP Server'
byteToSend = str.encode(msg)
print(byteToSend)
serverAddress = ("127.0.0.1", 20001)
bufferSize = 1024

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

client.sendto(byteToSend, serverAddress)

while(True):
    msgfrom = client.recvfrom(bufferSize)
    msgprint = "Message from Server {}".format(msgfrom)
    print(msg)
