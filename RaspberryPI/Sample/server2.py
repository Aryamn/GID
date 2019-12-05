import socket

msg = "Welcome to the Server!"
#  length = 10000000  #length that can be send in one datapacket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(5)

while True:
        clientsocket, address = s.accept()
        print("Listening from {address}")

        a = []
        a.append(msg)
        a.append(len(msg))

        clientsocket.send(bytes(a[0], "utf-8"))
