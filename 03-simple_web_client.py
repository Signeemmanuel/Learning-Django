import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating endpoint
mysocket.connect(("127.0.0.1", 9000))   # Making a connection to localhost port 9000

cmd = "GET http://127.0.0.1/remeo.html HTTP/1.0\r\n\r\n".encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(5012)
    if len(data) < 1:
        break
    print(data.decode())

mysocket.close()