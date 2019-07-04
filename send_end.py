import socket
import os
import binascii
from process_data import processing_data
import numpy as np
from matplotlib import pyplot as plt

f = open("test_switch0703.txt", "wb")

BUFSIZE = 2048
server_ip_port = ("192.168.1.101", 8080)
client_ip_port = ("192.168.1.100", 8080)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_ip_port)
# generate msg_end_sending to ask data
msg_end_sending = "\x28\x00\x01\x00\x02\x00\xA0\x35\x00\x01\x02\x00\x00\x00\x01\x00\x00\x80\x00"
server.sendto(msg_end_sending.encode("latin-1"), client_ip_port)

