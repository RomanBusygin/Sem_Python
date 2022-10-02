


bot = Bot(token = '5699740380:AAH8f6hNtBnCs_-fqN9e7WOB94FNBgkwJdA')


print('Server start')
@dp.message_handler(commands = ['start', 'help'])
async def all_commands(message: types.Message):
    await message.reply(f'/help\n')
