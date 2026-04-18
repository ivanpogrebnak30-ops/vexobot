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
        "👋 Привет, добро пожаловать в VexoShop 🇺🇦!\n"
        "🛍 Здесь ты можешь оформить первый заказ или задать любой вопрос.\n\n"
        "📨 Связь с менеджером: @livaxw",
        "Я бы ответил умно, но у меня нет лицензии на интеллект 🤖",
        "Секунду… я думаю… ой, всё 💀",
        "Ошибка 404: смысл не найден",
        "Я бот, но даже я не понял это сообщение 😄",
        "Ты это сейчас серьёзно написал? 👀",
        "Мой процессор сказал: «я устал» 💤",
        "Я пытался понять… честно… не получилось 🫠",
        "Это сообщение отправлено в параллельную вселенную 🌌",
        "Я завис… но красиво ✨",
        "Слишком сложно для моего железа 🧠",
        "Я это прочитал и теперь мне нужно лечь 🤖",
        "Это сейчас был запрос или заклинание? 🧙‍♂️",
        "Я пытался перевести… Google сдался 😶",
        "Слишком мощно, я не вывожу 😵"
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
