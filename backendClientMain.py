import websockets, json
import asyncio
import wss
import datetime


ConnectGcUrl = wss.wssGcUrl()
ConnectMainUrl = wss.wssConnectUrl

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
         
         # These print statements are really just for debugging

         js = ('{"action":"requestChat"}')
         await web.send(js)
         print("we have sent the first request") 
         run = True
         print("beggining the loop")
         while run: 
             
             name = await web.recv()
             print("this is the name: " + name) 
             f = open(name , "a") 

             message = await web.recv() 
             print(message) 
             f.write(message)
             f.close() 


             message = await web.recv()
             if (message == "CLOSECLOSECLOSE"): 
                 break


"""

The sendMessage function will send a message to the database (the Amazon s3 bucket) 
@param: Message: String value: What message are you trying to send? 
@param: groupchat: String value: What groupchat are you trying to send? 
@param: name: Userid that will send the function. TODO: Delete this later as it is really only useful for testing. 
The result of the function should be that the message is sent and updated to the groupchat bucket. In addition, it will be sent out to every user BESIDES this user. 

TODO: Error catching. What about poor networking issues? We do not have a fail safe for that. 

"""


async def sendMessage(message, name, groupchatId): 
    async with websockets.connect(ConnectGcUrl) as web: 
         
        # These print statements are really just for debugging

        print("we have started the send message function") 
        print("this is the message that we will send" + message) 
        print("this is the username we will send it from" + " " + name)
        js = ('{"action":"sendMessage", "message":"' + message + '", "name":"' + name + '", "time":"'+ str(datetime.datetime.now()) + '"}')
        await web.send(js)

"""

Always run recieve is a function that will always be running to keep the text files updated as the messages are recieved. 


"""


async def alwaysRunReceive():
    async with websockets.connect(ConnectGcUrl):
        pass
        # Print Statements are for Debugging purposes. 


        


asyncio.get_event_loop().run_until_complete(sendMessage("hello", "hello"))



