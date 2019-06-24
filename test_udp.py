import socket
import os

f = open("test123456.txt", "wb")

BUFSIZE = 2048
server_ip_port = ("192.168.1.101", 8080)
client_ip_port = ("192.168.1.100", 8080)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_ip_port)

# generate msg_shake_hand to shake hand
msg_shake_hand = chr(0x28)
msg_shake_hand += chr(0x00)
msg_shake_hand += chr(0x01)
msg_shake_hand += chr(0x00)
msg_shake_hand += chr(0x02)
msg_shake_hand += chr(0xA0)
msg_shake_hand += chr(0x35)
msg_shake_hand += chr(0x00)
msg_shake_hand += chr(0x01)
msg_shake_hand += chr(0x02)
msg_shake_hand += chr(0x00)
msg_shake_hand += chr(0x00)
msg_shake_hand += chr(0x00)
msg_shake_hand += chr(0x01)
msg_shake_hand += chr(0x00)
msg_shake_hand += chr(0x00)
msg_shake_hand += chr(0x08)
msg_shake_hand += chr(0x00)

# generate msg_ask_data to ask data
msg_ask_data = chr(0x28)
msg_ask_data += chr(0x00)
msg_ask_data += chr(0x01)
msg_ask_data += chr(0x00)
msg_ask_data += chr(0x02)
msg_ask_data += chr(0xA0)
msg_ask_data += chr(0x35)
msg_ask_data += chr(0x00)
msg_ask_data += chr(0x01)
msg_ask_data += chr(0x02)
msg_ask_data += chr(0x00)
msg_ask_data += chr(0x00)
msg_ask_data += chr(0x00)
msg_ask_data += chr(0x01)
msg_ask_data += chr(0x00)
msg_ask_data += chr(0x01)
msg_ask_data += chr(0x00)
msg_ask_data += chr(0x00)


# 1 shake hand
server.sendto(msg_shake_hand.encode(), client_ip_port)

# receive shake hand message
count = 0
for i in range(4):
# while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    count += 1
    print(count)

# 2 ask data
count = 0
server.sendto(msg_ask_data.encode(), client_ip_port)
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    print("data:", len(data))
    count += 1
    print(count)
    if count % 128 <= 64 and count % 128 > 0:
        f.write(data)
    # else:
    #     temp_data += data
    server.sendto(msg_ask_data.encode(), client_ip_port)
    # if count % 128 == 0:
    #     server.sendto(msg_ask_data.encode(), client_ip_port)

    if count > 500:
        break