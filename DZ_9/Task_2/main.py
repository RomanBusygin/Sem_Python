from aiogram import Bot, types, Dispatcher, executor
from Token import bot_token


bot = Bot(token = bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start', 'help'])
async def all_commands(msg: types.Message):
    await msg.reply(f'/help\n/see_phonebook')

@dp.message_handler(commands = ['see_phonebook'])
async def see_phonebook(msg: types.Message):
    await msg.reply()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

