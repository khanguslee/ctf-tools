import socket
from pwn import *

# Edit below to server you want to connect to
host = 'localhost'
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port)) 
message_length = 60

message = 'message-to-send\n'.encode()

print(message)
s.send(message)

r = s.recv(1024)
print(r)
s.close()

