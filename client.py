import asyncio
import websockets

async def send_messages(websocket):
    while True:
        # Prompt the user for a message
        message = await asyncio.get_event_loop().run_in_executor(None, input)

        # Send the message to the server
        await websocket.send(message)

async def receive_messages(websocket):
    try:
        while True:
            # Receive a message from the server
            response = await websocket.recv()
            print(f"Received: {response}")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")

async def chat():
    # Start two tasks concurrently
    async with websockets.connect("ws://localhost:5680") as websocket:
        await asyncio.gather(
            send_messages(websocket),
            receive_messages(websocket)
        )

if __name__ == "__main__":
    asyncio.run(chat())
