# TCP Client code that connects to a TCP Server
#
# Need to investigate the below
#
# Troubleshooting Notes:
# changing parameter target_host causes error
# changing the .sendall() payload returns an error

import socket

# Specify target website and port number
target_host = "www.google.com"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send data
client.sendall("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())

# Receive data
response = client.recv(4096)

print(response)
