import socket
import time
import numpy as np
import cv2

# capture = cv2.VideoCapture(0)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 12346))

while True:
    d = sock.recv(45000)
    # e = e + len(d)

    nparr = np.fromstring(d, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('frame', frame)
    time.sleep(2)
    c = cv2.waitKey(30)

    if(c==27):
        break

    print("read")