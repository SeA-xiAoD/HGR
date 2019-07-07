import socket
import os
import binascii
from process_data import processing_data
import numpy as np
from matplotlib import pyplot as plt

f = open("../data_0707/0/0.txt", "wb")

BUFSIZE = 2048
server_ip_port = ("192.168.1.101", 8080)
client_ip_port = ("192.168.1.100", 8080)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_ip_port)

# generate msg_start_sending to shake hand
msg_start_sending = "\x28\x00\x01\x00\x02\x01\xA0\x35\x00\x01\x02\x00\x00\x00\x01\x00\x00\x80\x00"

# generate msg_end_sending to ask data
msg_end_sending = "\x28\x00\x01\x00\x02\x00\xA0\x35\x00\x01\x02\x00\x00\x00\x01\x00\x00\x80\x00"

# send start message
print(server.sendto(msg_start_sending.encode("latin-1"), client_ip_port)) # latin-1 can avoid \xc2

# receive data
package_count = 0
frame_count = 0

data_buffer = None
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    package_count += 1

    if data_buffer is None:
        data_buffer = data
    else:
        data_buffer += data

    if package_count % 64 == 0:
        data_4_display = processing_data(data_buffer)
        x = np.arange(1, data_4_display.shape[1] +1)
        plt.ion()
        plt.clf()
        plt.title("test")
        for i in range(8):
            plt.xlabel("samples")
            plt.ylabel("Voltage /V")
            plt.subplot(4, 2, i+1)
            plt.ylim([0, 3.0])
            plt.plot(x, data_4_display[i])
            plt.title("ch" + str(i + 1))
            plt.tight_layout(1)
        plt.pause(0.0001)
        data_buffer = None
        package_count = 0
        frame_count += 1
        print(frame_count)
    
f.close()