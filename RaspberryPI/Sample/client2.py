import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((socket.gethostname() , 1236))

while True:
    fullmsg = ''
    newmsg = True
    while True:
        a = s.recv(16)
        if newmsg:
            size = int(a[1]) 
            newmsg = False

        fullmsg = fullmsg + a[0].decode("utf-8")

        if(len(fullmsg) == size):
            print("full msg recvd")
            print(fullmsg)
            newmsg = True
            fullmsg = ''

    print(fullmsg)