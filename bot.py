
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌐 Открыть Sfera VPN",
                web_app=WebAppInfo(
                    url="https://j798g6fzw8-sudo.github.io/sferas_vpn/"
                )
            )
        ]
    ]
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🌐 Добро пожаловать в Sfera VPN!\n\n"
        "Выбирай сервер и управляй своим аккаунтом.",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
