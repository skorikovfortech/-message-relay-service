from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html
from aiogram import Dispatcher
from app.bot.queries import add_user, get_user
from app.models import User

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    """
    Функция, которая активируется при команде '/start'.
    Проверяет: есть ли этот пользователь в бд или нет,
    если нет, то записывает в бд.
    """
    chat_username = message.chat.username
    chat_id = message.chat.id
    user_tg_id = message.from_user.id
    user = await get_user(user_tg_id)
    if not user:
        await add_user(chat_username, user_tg_id)

    await message.answer(
        f"Привет, {message.from_user.first_name}! Напиши мне сообщение что бы я его сохранил и отправил в Slack"
    )
