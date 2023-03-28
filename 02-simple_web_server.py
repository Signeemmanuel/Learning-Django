import socket

def createServer():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Creating endpoint
    try:
        server_socket.bind(('localhost', 9000))   # Listening to port 9000
        server_socket.listen(5) # Demand operating system to queue a maximum of 5 connections from clients
        while True:
            (client_socket, address) = server_socket.accept()   # Accepting client connection

            rd = client_socket.recv(5000).decode()
            pieces = rd.split('\n')
            if (len(pieces) > 0):
                print(pieces[0])
            data = "HTTP/1.0 200 OK\r\n"
            data += "content-type: text/html; charset: UTF-8\r\n"
            data += "\r\n"
            data += "<html><body><h1>Hello World!</h1></body></html>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_socket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")

    except Exception as exc:
        print("\nError:\n")
        print(exc)

    server_socket.close()


print("Access http://localhost:9000")
createServer()