import socket
import os

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
server.sendto(msg_start_sending.encode("latin-1"), client_ip_port) # latin-1 can avoid \xc2

# receive cache packages
for i in range(128):
    data, client_addr = server.recvfrom(BUFSIZE)
    print(i)

# receive data
package_count = 0
frame_count = 0
temp_data = None
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    package_count += 1

    if temp_data is None:
        temp_data = data
    else:
        temp_data += data
    
    if package_count % 64 == 0:
        package_count = 0
        f = open(os.path.join("../data_0707/6", str(frame_count) + ".txt"), "wb")
        f.write(temp_data)
        f.close()
        temp_data = None
        frame_count += 1
        print(frame_count)

    if frame_count == 20:
        server.sendto(msg_end_sending.encode("latin-1"), client_ip_port)
        break
    