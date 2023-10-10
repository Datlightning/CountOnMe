import socket
import threading
host = 0
port = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def broadcast(message): 
    for client in clients: 
        client.send(message)


def handle(client): 
    while True: 
        try: 
            message=client.recv(1024)
            broadcast(message) 
        except: 
            index = clients.index(client) 
            clients.remove(client) 
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!.'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def recieve(): 
    while True: 

        client, address = server.accept()
        print("connected with {}".format(str(address)))


        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)


        print('Nickname is {}'.format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        clint.send("connected to server!".encode('ascii'))
        

        thread = threading.Thread(target=handle, args =(client,))
        thread.start()


recieve()

        
