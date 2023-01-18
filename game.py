
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://172.16.173.86:8080/") as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

asyncio.run(hello())


