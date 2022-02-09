import socket
import threading
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 80

sock.bind((ip,port))

sock.listen(1)

conn, addr = sock.accept()

def receive_and_print():
    for message_in in iter(lambda: conn.recv(1024).decode(), ''):
        print(":", message_in)

background_thread = threading.Thread(target=receive_and_print)
background_thread.daemon = True
background_thread.start()

while True:
    message_out = input()
    if message_out == '-1':
        background_thread.stop() 
        sock.close()
        break 
    conn.send(message_out.encode())