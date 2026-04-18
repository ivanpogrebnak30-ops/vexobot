import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8333349750:AAFpxCIU3z5ly__Y1AhK1Dkg2f1wC7W5rCM"
ADMIN_ID = 7908377164  # 👈 вставь свой Telegram ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 🔘 кнопки
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Каталог")],
        [KeyboardButton(text="🛒 Заказать")],
        [KeyboardButton(
            text="🌐 Сайт",
            web_app=WebAppInfo(url="https://gaze-yielding-firefly.tilda.ws/")
        )]
    ],
    resize_keyboard=True
)

# 🚀 старт
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 Привет, добро пожаловать в VexoShop 🇺🇦"
       " Свой первый заказ вы можете заказать, а также задать любой вопрос у нашего менеджера
        📨 Связь с менеджером: @livaxw\n\n",
        reply_markup=kb
        
    )

# 📦 каталог
@dp.message(F.text == "📦 Каталог")
async def catalog(message: types.Message):
    await message.answer(
        "🔥 Каталог:\n\n"
        "• Elf Bar\n"
        "• HQD\n"
        "• Жидкости\n\n"
        "Нажми 'Заказать' 👇"
    )

# 🛒 заказ
@dp.message(F.text == "🛒 Заказать")
async def order(message: types.Message):
    text = (
        f"🛒 НОВЫЙ ЗАКАЗ\n\n"
        f"👤 @{message.from_user.username}\n"
        f"🆔 {message.from_user.id}"
    )

    # 📩 отправка тебе
    await bot.send_message(ADMIN_ID, text)

    # ответ клиенту
    await message.answer("✅ Заказ принят! Менеджер вам напишет 👌")

# 😂 если пишет что-то не то
@dp.message()
async def jokes(message: types.Message):
    jokes = [
        "🤔 Нажми кнопку ниже",
        "😂 Я понимаю только кнопки",
        "🙃 Не ломай меня",
        "🧠 Попробуй нажать 'Каталог'",
        "😄 Я бот, не гадаю"
    ]
    await message.answer(random.choice(jokes))

# ▶ запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
