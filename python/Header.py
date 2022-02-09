import cv2
import pickle
import socket
import threading
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = '127.0.0.1'
port = 80
to_ip = '127.0.0.1'
to_port = 8080

sock.bind((ip, port))


# Start Video instance
vid = cv2.VideoCapture(0)

image_num = 0
BYTE = 40000
while(cv2.waitKey(25) & 0xFF != ord('q')):
    # read image
    ret, frame = vid.read()
    encoded,buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
   
    # convert array to binary
    bufferbytes = pickle.dumps(buffer)

    # Header data
    image_num = (image_num%1000) +1
    total_length =  len(bufferbytes)
    packet_num = total_length // BYTE
    if total_length % BYTE != 0:
        packet_num += 1

    total_packets = packet_num
    print(packet_num)

    x = 0
    while x < total_length:
         
        packet = bytes(f'{packet_num:<{4}}{image_num:<{4}}{total_packets:<{4}}',"utf-8") + bufferbytes[x:x+min(total_length -x,BYTE)]
        x += min(total_length -x,BYTE)
        packet_num -= 1

        # print(len(bufferbytes[x:x+min(total_length -x,1024)]), len(packet))

        # send packet
        time.sleep(0.025)
        sock.sendto(packet,(to_ip,to_port))

vid.release()
