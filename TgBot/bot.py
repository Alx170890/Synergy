import logging
from pathlib import Path
from argparse import ArgumentParser
from aiogram import Bot, Dispatcher, executor, types


parser = ArgumentParser()
parser.add_argument('-t', '--token', help='Bot token', required=True)
args = parser.parse_args()


bot = Bot(token=args.token)
dp = Dispatcher(bot)


__all__ = ['send_welcome', 'echo']


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot Alex!\nYou like a pizza?")


@dp.message_handler()
async def echo(message: types.Message):
    mess = message.text
    if mess == 'yes':
        await message.answer(f'Cool! You can order pizza at: https://dominospizza.ru/')
    else:
        await message.reply("You like a pizza?")


if __name__ == '__main__':
    logging.root.setLevel(logging.INFO)
    executor.start_polling(dp, skip_updates=True)
