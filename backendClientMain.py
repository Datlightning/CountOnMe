import websockets, json
import asyncio
import wss
import time


ConnectGcUrl = wss.wssGcUrl()


"""


This function enables connect access to the websockets Aws API gateway



"""



async def connectMain():

     async with websockets.connect(ConnectMainUrl) as web:
         await web.send("{}")
         response = await web.recv()
         return response
"""

The Recieve Gcs function is code that should be run on initialization of the application 
It will update all existing Gcs of the user to be matched with the groupchats on the serverside end
No parameters, no return
The exit() method at the end of the function ensures that the file is closed afterwards. 
We are undfortuantely already running a multi-thread intensive program and I want to close as many threads as necessary. 

TODO: Error Catching: What happens when the networking is poor? Need to create a failsafe. 

"""
async def recieveGcs(): 
     async with websockets.connect(ConnectGcUrl) as web: 
         print("we have started the function")  

         js = ('{"action":"requestChat"}')
         await web.send(js)
         print("we have sent the first request") 
         run = True
         print("beggining the loop")
         while run: 
             
             name = await web.recv()
             print("this is the name: " + name) 
             f = open(name, "a") 

             message = await web.recv() 
             print(message) 
             f.write(message)
             f.close() 


             message = await web.recv()
             if (message == "CLOSECLOSECLOSE"): 
                 break
        exit()

"""

The sendMessage function will send a message to the database (the Amazon s3 bucket) 
@param: Message: String value: What message are you trying to send? 
@param: groupchat: String value: What groupchat are you trying to send? 

The result of the function should be that the message is sent and updated to the groupchat bucket. In addition, it will be sent out to every user BESIDES this user. 

TODO: Error catching. What about poor networking issues? W do not have a fail safe for that. 

"""


async def sendMessage(message): 
    asyncio.get_event_loop().run_until_complete(connectMain()) 
    async with websockets.connect(ConnectGcUrl) as web: 
        print("we have started the send message function") 
        print("this is the message that we will send" + message) 

        


asyncio.get_event_loop().run_until_complete(recieveGcs())



