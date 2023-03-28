import socket

# Creating a Socket object
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Creating endpoint
my_socket.connect(("data.pr4e.org", 80))    # Making a connection at port 80 to data.pr4e.org

# Making a request
cmd = "GET http://data.pr4e.org/page1.html HTTP/1.0\r\n\r\n".encode()
my_socket.send(cmd)

# Getting Server's Response
while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

my_socket.close()