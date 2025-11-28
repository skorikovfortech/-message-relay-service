from app.core.settings import bot_token
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
import logging
from app.bot.handler import dp


async def main():
    bot = Bot(bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if "__main__" == __name__:
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
