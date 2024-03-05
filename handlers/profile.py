import sqlite3

from aiogram import types, Dispatcher

import const
from config import bot
from database.bot_db import Database
from keyboards.profile_inline_buttons import (

    like_dislike_keyboard,
)
import random
import re


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.sql_select_profile(
        tg_id=call.from_user.id
    )
    print(profile)
    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=profile['nickname'],
                    bio=profile['bio'],
                    age=profile['age'],
                    sign=profile['sign'],
                ),

            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U did not registered\n"
                 "Please register to view ur profile"
        )


async def random_filter_profile_call(call: types.CallbackQuery):
    print(call.message.caption)

    db = Database()
    profiles = db.sql_select_all_profiles(
        tg_id=call.from_user.id
    )
    print(profiles)
    if not profiles:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='U have liked all profiles, come later!'
        )
        return

    random_profile = random.choice(profiles)
    with open(random_profile['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=const.PROFILE_TEXT.format(
                nickname=random_profile['nickname'],
                bio=random_profile['bio'],
                age=random_profile['age'],
                hobby=random_profile['hobby'],
                gpa=random_profile['edu'],
                sign=random_profile['sign'],
            ),
            reply_markup=await like_dislike_keyboard(
                tg_id=random_profile['telegram_id']
            )
        )


async def detect_like_call(call: types.CallbackQuery):
    # print(call.data)
    # print(call.data[5:])
    # print(call.data.replace("like_", ""))
    owner = re.sub('llike_', "", call.data)
    print(owner)
    db = Database()
    db.sql_insert_like(
        owner=owner,
        liker=call.from_user.id
    )
    await call.message.delete()
    await random_filter_profile_call(call=call)


async def detect_dislike_call(call: types.CallbackQuery):
    # print(call.data)
    # print(call.data[5:])
    # print(call.data.replace("like_", ""))
    owner = re.sub('dislike_', "", call.data)
    db = Database()
    db.sql_insert_dislike(
        owner=owner,
        disliker=call.from_user.id
    )

    await call.message.delete()
    await random_filter_profile_call(call=call)


async def delete_profile(call: types.CallbackQuery):
    data = Database()
    profile = data.sql_select_profile(call.from_user.id)
    if profile:
        data.delete_profile(call.from_user.id)
    else:
        await bot.send_message(chat_id=call.from_user.id, text="you dont have registered , please sign up!")


def register_profile_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        random_filter_profile_call,
        lambda call: call.data == "random_profiles"
    )
    dp.register_callback_query_handler(
        detect_dislike_call,
        lambda call: 'dislike_' in call.data
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: 'llike_' in call.data
    )
    dp.register_callback_query_handler(
        delete_profile,
        lambda call: call.data == 'delete'
    )
