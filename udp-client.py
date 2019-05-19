import socket

# Specify target website and port number
target_host = "127.0.0.1"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect the client
client.sendto("AAABBBCCC".encode(), (target_host, target_port))

# Send data
#client.sendall("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())

# Receive data
data,addr = client.recvfrom(4096)

print(data)

