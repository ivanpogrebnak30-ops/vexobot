import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import CommandStart

# 🔧 логирование
logging.basicConfig(level=logging.INFO)

# 🔑 токен
BOT_TOKEN = os.getenv("8333349750:AAFpxCIU3z5ly__Y1AhK1Dkg2f1wC7W5rCM")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 🌐 клавиатура
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог")],
        [KeyboardButton(text="💰 Цены"), KeyboardButton(text="📨 Связь")],
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
        "👋 Добро пожаловать в VexoShop!\n\n"
        "Выбери действие ниже 👇",
        reply_markup=kb
    )

# 🛍 каталог
@dp.message(F.text == "🛍 Каталог")
async def catalog(message: types.Message):
    await message.answer(
        "🔥 Наш ассортимент:\n\n"
        "• Одноразки (Elf Bar, HQD)\n"
        "• Жидкости 30ml / 60ml\n"
        "• POD-системы\n\n"
        "Напиши, что интересует 👇"
    )

# 💰 цены
@dp.message(F.text == "💰 Цены")
async def prices(message: types.Message):
    await message.answer(
        "💰 Примерные цены:\n\n"
        "• Одноразки — от 250 грн\n"
        "• Жидкости — от 150 грн\n"
        "• POD-системы — от 600 грн\n\n"
        "Точную цену уточняй 👇"
    )

# 📩 связь
@dp.message(F.text == "📨 Связь")
async def contact(message: types.Message):
    await message.answer(
        "📨 Менеджер: @livaxw\n"
        "Напиши для заказа или консультации 💬"
    )

# 💬 ответы на текст
@dp.message(F.text)
async def chat(message: types.Message):
    text = message.text.lower()

    if "привет" in text:
        await message.answer("Привет 👋 Чем помочь?")
    elif "однораз" in text:
        await message.answer("Есть Elf Bar и HQD 🔥 Напиши в личку: @livaxw")
    elif "жидк" in text:
        await message.answer("Есть разные вкусы 🍓🥭 Напиши менеджеру: @livaxw")
    else:
        await message.answer(
            "🤷‍♂️ Не понял, выбери кнопку ниже или напиши менеджеру: @livaxw"
        )

# ▶️ запуск
async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())