import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234
IP_ADDRESS = (SERVER, PORT)
CLIENTS = {}

def setup():
    global SERVER, PORT, IP_ADDRESS
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(IP_ADDRESS)
    server.listen(100)
    print("Server is running on {}:{}".format(SERVER, PORT))
    while True:
        client_socket, client_address = server.accept()
        print("New connection from {}:{}".format(client_address[0], client_address[1]))
        # Handle the client connection here
        file_name = client_socket.recv(1024).decode()
        file_size = client_socket.recv(1024).decode()
        CLIENTS[client_socket] = (client_address, file_name, file_size)

def acceptConnections():
    while True:
        client_socket, client_address = SERVER.accept()
        print("New connection from {}:{}".format(client_address[0], client_address[1]))
        # Handle the client connection here
        file_name = client_socket.recv(1024).decode()
        file_size = client_socket.recv(1024).decode()
        CLIENTS[client_socket] = (client_address, file_name, file_size)

if __name__ == "__main__":
    setup()
    accept_thread = threading.Thread(target=acceptConnections)
    accept_thread.start()
