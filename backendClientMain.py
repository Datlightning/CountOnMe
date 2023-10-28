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
        sendValue = ('{"action":"sendMessage", "message":"' + message + '", "name":"' + name + '", "time":"'+ str(datetime.datetime.now()) + ',"groupchatId":"' + groupchatId + '"' +'}')
        
        await web.send(sendValue)
        print(sendValue)

        # print statement is placed after method call for a reason: 
        # if the sendValue variable is printed, then this means that it was sent as well. 

"""

Always run recieve is a function that will always be running to keep the text files updated as the messages are recieved. 


"""


async def alwaysRunReceive():
    async with websockets.connect(ConnectGcUrl) as web:
        # We want this code to be eternally running. Every message that is sent during the time of the app's opening should be immediately written to the groupchats. 
        while True: 
            print("Initializing run function.")

            # asyncio.wait_for basically is the same thing as an await call but instead of awaiting forever, it has a timeout. 

            message = await web.recv()
            message = json.loads(message)
            f = open(message["groupchatId"], "a")
            f.write(message["message"])
            f.write(message["user"])
            f.write(message["time"])
            f.close()
            print(message)
            # Print Statements are for Debugging purposes. 


# We want these two functions to run at the same time, on different threads, asynchronously, because networking. 

"""

The whole concept of asynchronous code can seem complicated, but what helped me was this stack overflow thread. 
https://stackoverflow.com/questions/748175/asynchronous-vs-synchronous-execution-what-is-the-difference#748189

"""

"""

Threading is not psosible so I am manually just switching in between the tasks over and over again. 
This is a terrible practice, but it is also 11:17 pm on a Friday Night. I am ready to quit life. Please. 

TODO: Make this more efficient man. 

TODO: Figure out how to optimize this stuff in a singular thread. Potentially time.sleep()s? 

"""


async def main():
    await asyncio.gather(alwaysRunReceive(), sendMessage("hello", "Ruthvik", "hey"))

while True: 
    asyncio.run(main())