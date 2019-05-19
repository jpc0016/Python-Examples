import socket

# Specify target website and port number
target_host = "127.0.0.1"
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

