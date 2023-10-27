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

async def recieveGcs(): 
     async with websockets.connect(ConnectGcUrl) as web: 
         

         js = ('{"action":"requestChat"}')
         await web.send(js)

         run = True
         while run: 
            
             name = await web.recv()
            
             f = open(name, "a") 

             message = await web.recv() 
             print(message) 
             f.write(message)
             f.close() 


             message = await web.recv()
             if (message == "CLOSECLOSECLOSE"): 
                 break




asyncio.get_event_loop().run_until_complete(recieveGcs())



