import asyncio
import logging
import os
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

jokes = [
    "Ошибка 404 😄",
    "Я бот и я живой 🤖",
    "Слишком сложно 🧠"
]

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("👋 Бот работает!")

@dp.message(F.text)
async def chat(message: types.Message):
    await message.answer(random.choice(jokes))


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())