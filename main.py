from aiogram import Bot, Dispatcher
from app.handlers import router
import asyncio
import os
from aiohttp import web

# Get port from environment variable or use 10000 as default
PORT = int(os.environ.get("PORT", 10000))


# Create a simple web server to meet Render's requirements
async def handle_request(request):
    return web.Response(text="Telegram Bot is running!")


async def setup_web_server():
    app = web.Application()
    app.router.add_get('/', handle_request)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()

    print(f"Web server started on port {PORT}")


async def main():
    # Initialize bot with token (it's generally better to use environment variables for tokens)
    bot_token = "7627299223:AAEecfLK-l1JrofjSAeUoU36RZ7-rZVXenc"
    bot = Bot(token=bot_token)
    dp = Dispatcher()

    # Start web server
    await setup_web_server()

    # Include router with handlers
    dp.include_router(router)

    # Start the bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")