import socket
import threading
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = '127.0.0.1'
port = 8080
to_ip = '127.0.0.1'
to_port = 80

sock.bind((ip, port))


def receive_and_print():
    # data, addr = sock.recvfrom(1024)
    # message = data.decode()
    # print(":", message) 
    for message_in in iter(lambda: sock.recvfrom(1024)[0].decode(), '\n'):
        print(":", message_in) 

background_thread = threading.Thread(target=receive_and_print)
background_thread.daemon = True
background_thread.start()


while True:
    msg = input()
    encoded_msg = msg.encode()
    sock.sendto(encoded_msg,(to_ip,to_port))
