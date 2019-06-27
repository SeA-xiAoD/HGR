import socket
import os
import binascii

f = open("test_switch.txt", "wb")

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

# receive cache packages
for i in range(64):
    data, client_addr = server.recvfrom(BUFSIZE)
    print(i)

# receive data
count = 0
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    count += 1
    print(count)
    f.write(data)
    if count >= 320:
        server.sendto(msg_end_sending.encode("latin-1"), client_ip_port)
        break
    
f.close()