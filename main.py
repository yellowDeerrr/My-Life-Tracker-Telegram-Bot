from aiogram import Bot, Dispatcher
from app.handlers import router
import asyncio

async def main():
    bot = Bot(token='7627299223:AAEecfLK-l1JrofjSAeUoU36RZ7-rZVXenc')
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")