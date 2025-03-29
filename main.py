from aiogram import Bot, Dispatcher
from app.handlers import router
import asyncio
import socket

async def main():
    bot = Bot(token='7627299223:AAEecfLK-l1JrofjSAeUoU36RZ7-rZVXenc')
    dp = Dispatcher()

    asyncio.create_task(start_server(443))

    dp.include_router(router)
    await dp.start_polling(bot)

async def handle_client(client_socket, client_address):
    try:
        data = client_socket.recv(1024)
        print(f"Received from {client_address}: {data.decode()}")
        client_socket.send(b"Hello From Telegram Bot!")
        client_socket.close()
    except Exception as e:
        print(f"Customer processing error: {e}")

async def start_server(port_number):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port_number))
        server_socket.listen(5)
        print(f"Server is listening {port_number}")

        while True:
            client_socket, client_address = await asyncio.to_thread(server_socket.accept)
            print(f"Connection from {client_address}")
            asyncio.create_task(handle_client(client_socket, client_address))

    except Exception as e:
        print(f"Server Error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")