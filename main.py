import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8333349750:AAFpxCIU3z5ly__Y1AhK1Dkg2f1wC7W5rCM"
ADMIN_ID = 7908377164 # 👈 твой Telegram ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 📦 временное хранение выбора
user_orders = {}

# 🔘 главное меню
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог")],
        [KeyboardButton(text="💰 Цены")],
    ],
    resize_keyboard=True
)

# 📦 каталог
catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Elf Bar"), KeyboardButton(text="HQD")],
        [KeyboardButton(text="Жидкость")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)

# 🛒 кнопка заказа
order_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Заказать")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)

# 🚀 старт
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("👋 Добро пожаловать!", reply_markup=main_kb)

# 📦 каталог
@dp.message(F.text == "🛍 Каталог")
async def catalog(message: types.Message):
    await message.answer("Выбери товар 👇", reply_markup=catalog_kb)

# ⬅ назад
@dp.message(F.text == "⬅ Назад")
async def back(message: types.Message):
    await message.answer("Главное меню 👇", reply_markup=main_kb)

# 💰 цены
@dp.message(F.text == "💰 Цены")
async def prices(message: types.Message):
    await message.answer(
        "💰 Цены:\n"
        "• Elf Bar — 250 грн\n"
        "• HQD — 250 грн\n"
        "• Жидкость — 150 грн"
    )

# 📦 выбор товара
@dp.message(F.text.in_(["Elf Bar", "HQD", "Жидкость"]))
async def choose_product(message: types.Message):
    user_orders[message.from_user.id] = message.text
    await message.answer(
        f"Ты выбрал: {message.text}\nНажми заказать 👇",
        reply_markup=order_kb
    )

# 🛒 заказ
@dp.message(F.text == "✅ Заказать")
async def order(message: types.Message):
    product = user_orders.get(message.from_user.id, "Неизвестно")

    # сообщение тебе
    text = (
        f"🛒 НОВЫЙ ЗАКАЗ!\n\n"
        f"👤 @{message.from_user.username}\n"
        f"📦 Товар: {product}"
    )

    await bot.send_message(ADMIN_ID, text)

    await message.answer("✅ Заказ отправлен! С тобой скоро свяжутся", reply_markup=main_kb)

# 😂 шутки
@dp.message()
async def jokes(message: types.Message):
    jokes = [
        "🤔 Я не понял, но звучит круто",
        "😂 Нажми кнопку, не пугай меня",
        "🧠 Ошибка: человек слишком креативный",
        "🙃 Я работаю только с кнопками",
        "😄 Ты пытаешься меня сломать?"
    ]
    await message.answer(random.choice(jokes))

# ▶ запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
