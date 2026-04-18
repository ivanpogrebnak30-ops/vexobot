import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8333349750:AAFpxCIU3z5ly__Y1AhK1Dkg2f1wC7W5rCM"  # 👈 вставь сюда токен

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 🔘 Кнопки
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

# 🚀 Старт
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в VexoShop!\n\nВыбери действие ниже 👇",
        reply_markup=kb
    )

# 📦 Каталог
@dp.message(F.text == "🛍 Каталог")
async def catalog(message: types.Message):
    await message.answer(
        "🔥 Наш ассортимент:\n\n"
        "• Одноразки (Elf Bar, HQD)\n"
        "• Жидкости 30ml / 60ml\n"
        "• POD-системы\n\n"
        "Напиши, что интересует 👇"
    )

# 💰 Цены
@dp.message(F.text == "💰 Цены")
async def prices(message: types.Message):
    await message.answer(
        "💰 Примерные цены:\n\n"
        "• Одноразки — от 250 грн\n"
        "• Жидкости — от 150 грн\n"
        "• POD-системы — от 600 грн\n"
    )

# 📩 Связь
@dp.message(F.text == "📨 Связь")
async def contact(message: types.Message):
    await message.answer("📨 Менеджер: @livaxw")

# 😂 Общий чат + шутки
@dp.message(F.text)
async def chat(message: types.Message):
    text = message.text.lower()

    # ❌ если команда неправильная
    if text.startswith("/"):
        jokes = [
            "🤔 Такой команды не существует",
            "😅 Ты это сам придумал?",
            "🚫 Команда не найдена",
            "👀 Я такого не знаю",
            "🫠 Попробуй /start"
        ]
        await message.answer(random.choice(jokes))
        return

    # ✅ нормальные ответы
    if "привет" in text:
        await message.answer("Привет 👋 Чем помочь?")
    elif "однораз" in text:
        await message.answer("Есть Elf Bar и HQD 🔥 Пиши: @livaxw")
    elif "жидк" in text:
        await message.answer("Есть разные вкусы 🍓🥭 Пиши: @livaxw")

    # 😂 если не понял
    else:
        jokes = [
            "🤷‍♂️ Я не понял, но звучит интересно",
            "😂 Это не команда, но мне нравится",
            "🧠 Обрабатываю... ошибка 404",
            "🙃 Попробуй нажать кнопку ниже",
            "😄 Я пока не такой умный"
        ]
        await message.answer(random.choice(jokes))


# ▶️ Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
