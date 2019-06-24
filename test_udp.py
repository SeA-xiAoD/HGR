import socket
import os

f = open("test123456.txt", "wb")

BUFSIZE = 2048
server_ip_port = ("192.168.1.102", 8080)
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
print(server.sendto(msg_shake_hand.encode(), client_ip_port))

# 2 ask data
count = 0
server.sendto(msg_ask_data.encode(), client_ip_port)
temp_data = None
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    print("data:", data)
    print(count)
    if temp_data == None:
        temp_data = data
    else:
        temp_data += data
    
    # server.sendto(msg_ask_data.encode(), client_ip_port)

    count += 1
    if count == 150:
        f.write(temp_data)
        break