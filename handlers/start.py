import sqlite3
from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import  _create_link

import const
from config import MEDIA_DESTINATION
from config import bot
from database import bot_db
from keyboards import start_inline_buttons

import const

async def start_button(message: types.Message):
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    print(message.get_full_command())
    command = message.get_full_command()
    if command[1] != "":
        link = await _create_link("start", payload=command[1])
        owner = db.sql_select_user_by_link(
            link=link
        )
        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text='U can not use ur own link!!!'
            )
            return

        try:
            db.sql_insert_referral(
                owner=owner['telegram_id'],
                referral=message.from_user.id
            )
            db.sql_update_balance(
                owner=owner['telegram_id']
            )
        except sqlite3.IntegrityError:
            pass

    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=const.START_MENU_TEXT.format(
    #         user=message.from_user.first_name
    #     ),
    #     reply_markup=await start_inline_buttons.start_keyboard()
    # )

    with open(MEDIA_DESTINATION + "file_2.jpg", 'rb') as photo:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=photo,
            caption=const.START_MENU_TEXT.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_inline_buttons.start_keyboard()

        )


# async def ban_info_button(message: types.Message):
#     db = bot_db.Database()
#     db.sql_select_ban_user(
#         tg_id=message.from_user.id,

# )

# await bot.send_message(
#     chat_id=message.from_user.id,
#     text=const..format(
#         user=message.from_user.first_name
#     ),
#     reply_markup=await start_inline_buttons.start_keyboard()


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start']
    )

