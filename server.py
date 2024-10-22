import asyncio
import websockets

connected_clients = set()

async def handle_client(websocket):
    # Add new client to the connected clients
    connected_clients.add(websocket)
    print(f"CONNECTED: {websocket.id}")

    try:
        # Listen for messages from the client
        async for message in websocket:
            # Broadcast the message to all other connected clients
            for client in connected_clients:
                if client in connected_clients and client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Remove the client from the connected clients
        connected_clients.remove(websocket)
        print(f"DISCONNECTED: {websocket.id}")

async def main():
    server = await websockets.serve(handle_client, "localhost", 5680)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
