import socket
import threading
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 80

sock.connect((ip,port))


def receive_and_print():
    for message_in in iter(lambda: sock.recv(1024).decode(), ''):
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
    sock.send(message_out.encode())





# import socket
# import sys

# s = socket.socket()
# s.connect((sys.argv[1], int(sys.argv[2])))
# name = input(str("Please enter your username : "))
# print(" Connected to chat server")
# s.send(name.encode())

# def receive_and_print():
#     for message in iter(lambda: s.recv(1024).decode(), ''):
#         print(":", message)
#         print("")
# import threading
# background_thread = threading.Thread(target=receive_and_print)
# background_thread.daemon = True
# background_thread.start()

# while 1:
#     s.send(input("Please enter your message: ").encode())
#     print("Sent")
#     print("")