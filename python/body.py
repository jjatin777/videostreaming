import cv2
import pickle
import socket
import threading
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = '127.0.0.1'
port = 8080
to_ip = '127.0.0.1'
to_port = 80

sock.bind((ip, port))

BYTE = 40000 + 12
def receive_and_print():

    reciever_list =[None] * (1000)
    while True:
        
        packet ,addr = sock.recvfrom(BYTE)
        total_packets = int(packet[8:12])
        reciever_list[int(packet[:4])] = packet[12:]
        curr_image_num = int(packet[4:8])
        count = 1
        # print("\n new", total_packets)
        # print('(',int(packet[:4]),int(packet[4:8]),')', end = ' ')
        try:
            while(count < total_packets):
                count += 1
                # sock.settimeout(2)
                packet,addr = sock.recvfrom(BYTE)
                # print('(',int(packet[:4]),int(packet[4:8]),')', end = ' ')
                if curr_image_num < int(packet[4:8]):
                    count = 1
                    curr_image_num = int(packet[4:8])
                    total_packets = int(packet[8:12])
                    reciever_list[int(packet[:4])] = packet[12:]
                    # print("\n new", total_packets)

                elif curr_image_num == int(packet[4:8]):
                    reciever_list[int(packet[:4])] = packet[12:]
           
        except Exception:
            print("close")

        # reciever_list = sorted(reciever_list, key = lambda x: x[0], reverse = True)
        recieved_msg = b''

        for index in range(total_packets,0,-1):
            recieved_msg += reciever_list[index]

        try:
            image = pickle.loads(recieved_msg)
            buf = cv2.imdecode(image,1)
            # ord('q') returns the Unicode code point of q
            # cv2.waitkey(1) returns a 32-bit integer corresponding to the pressed key
            cv2.imshow('frame', buf)
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except Exception as e:
            print(e)
            break

    # Closes all the frames
    cv2.destroyAllWindows()

background_thread = threading.Thread(target=receive_and_print)
background_thread.daemon = True
background_thread.start()

while True:

    
    continue