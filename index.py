import asyncio
import logging 
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import TOKEN

TOKEN = "8147775201:AAFCadtCn0GF09ksKHi3ZQslJOzYmgdq6SQ"
bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Найти информацию", callback_data="find_info")],
            [InlineKeyboardButton(text="Связаться", callback_data="contact")],
            [InlineKeyboardButton(text="о боте", callback_data="about")]    
        ]
    )
    return keyboard

# Команда /start
@dp.message(Command("start"))
async def start(message: types.message):
    await message.answer(
        "Привет! Это тестовый бот!",
        reply_markup=get_keyboard()
    )



@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "find_info":
        await callback.message.answer("Введите информацию для поиска")
    elif callback.data == "contact":
        await callback.message.answer("Напишите нам в личку: @LuckyMen000")
    elif callback.data == "about":
        await callback.message.answer("Это наш на библиотеке aiogram")
    
    await callback.answer()

# Запуск бота 
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())