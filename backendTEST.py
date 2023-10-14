import socket

def start_server():
    server_ip = "0.0.0.0"  # Listen on all available interfaces
    server_port = 12345    # Choose a port (make sure it's not used by other services)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Server is listening on {server_ip}:{server_port}")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Client: {message}")
        response = input("You: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    start_server()

