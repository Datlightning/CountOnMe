import socket
import threading
host = "192.168.0.64"
port = 5555


class client(): 
    
    # problems is a messed up way to word it, but consider it a STRING list of all of the problems they have 
    # preference is the number of people that they want in their thing uyk w i mean
    def __init__(name, address, password, problems, preference):
        self.name = name
        self.address = address
        self.password = password
        self.problemms = problems
        self.preference = preference 
        






server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []


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

#man, i am adding this comment literally just to test if git works and thats it lmao. 

# TODO: 
# create text file or sql database shit to add SOMETHING 
recieve()

        
