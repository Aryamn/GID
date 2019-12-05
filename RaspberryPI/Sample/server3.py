import socket
import cv2
import numpy as np
import time

HOST = socket.gethostname()
PORT = 12346

print(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

capture = cv2.VideoCapture(0)

conn, addr = s.accept()

while True:
    
    ret, frame = capture.read()
    image = cv2.imencode('.jpg', frame)[1].tostring() 
    conn.sendall(image)