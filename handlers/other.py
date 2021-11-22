from aiogram import types,Dispatcher
from create_bot import dp
import json, string, os

# @dp.message_handler()
async def echo_send(message: types.Message):
    with open('mat.json', 'r', encoding="utf-8") as f:
        pick = json.load(f)
        if  {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(pick)) != set():
            await message.reply(f'Маты запрещены')
            await message.delete()


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
