import sqlite3

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import const
from config import bot
from database.bot_db import Database
class Complains(StatesGroup):
    who=State()



async def complain(mes:types.Message):
    await bot.send_message(
        chat_id=mes.from_user.id,
        text="Who broke the rule?(write  first name)"
    )

    await Complains.who.set()

async def waiting_first_name(message:types.Message,state:FSMContext):
    data = Database()
    name = data.select_first_name_telegram_user_table(message.text)

    if (name):
        await bot.send_message(chat_id=name[0][1],text="u will be bannned if u not stop ur  actions")
        await state.finish()
    else:
        await bot.send_message(chat_id=message.from_user.id, text="We couldnt find the user .Try again")
        await state.finish()
def register_complains(dp:Dispatcher):
    dp.register_message_handler(complain,commands='complain')
    dp.register_message_handler(waiting_first_name,state=Complains.who,content_types=['text'])