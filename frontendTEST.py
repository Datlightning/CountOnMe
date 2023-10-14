import socket

def start_client():
    server_ip = "SERVER_PUBLIC_IP"  # Replace with the public IP of your server
    server_port = 12345             # Make sure it's the same port as in the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))
        if message == "exit":
            break
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

