import socket
import threading 

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(("192.168.0.64", 5555)) 

def receive(): 
    while true: 
        try: 
            #Recieve Message from Server
            # if nick send nickname 

            message = client.recv(1024).decode('ascii')
            if message == 'NICK': 
                client.send(nickname.encode('ascii'))
            else: 
                print(message)
                
        except: 
            
            print("An error occured!:") 
            client.close() 
            break 

def write(): 
    while True: 
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receiveThread = threading.Thread(target=receive) 
receiveThread.start() 

writeThread = threading.Thread(target=write)
write_thread.start()

