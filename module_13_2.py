"""
Нужные версии для 13 и 14 модулей и вашего виртуального окружения находятся здесь:
aiogram==2.25.1
aiohttp==3.8.6
aiosignal==1.3.1
async-timeout==4.0.3
attrs==23.2.0
Babel==2.9.1
certifi==2024.7.4
charset-normalizer==3.3.2
frozenlist==1.4.1
idna==3.7
magic-filter==1.0.12
multidict==6.0.5
pytz==2024.1
yarl==1.9.4
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
