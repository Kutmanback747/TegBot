import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import bot_db
# from keyboards import start_inline_buttons
import const
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac_sign = State()
    education = State()
    hobby = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Send me ur nickname"
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur BIO!'
    )
    await RegistrationStates.next()


async def load_bio(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="How old r u ?\n"
             "(Send me only numeric text)\n"
             "Example:27 or 28"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        int(message.text)
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="I told u send me only numeric text"
        )

        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = int(message.text)
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Now send me sign of your Zodiac🐾'
    )

    await RegistrationStates.next()


async def load_zodiac_sign(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['sign'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me ur GPA of GRADUATING\n"
             ""
    )
    await RegistrationStates.next()


async def load_education(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['edu'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me ur list of hobbies \n"
             ""
    )
    await RegistrationStates.next()


async def load_hobby(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me ur photo\n"
             "only in photo format"
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = bot_db.Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )

    profile=db.sql_select_profile(message.from_user.id)
    if profile is None:
        async with state.proxy() as data:
            db.sql_insert_profile(
                tg_id=message.from_user.id,
                nickname=data['nickname'],
                bio=data['bio'],
                age=data['age'],
                sign=data['sign'],
                edu=data['edu'],
                hobby=data['hobby'],
                photo=path.name

            )
        with open(path.name, "rb") as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['bio'],
                    age=data['age'],
                    sign=data['sign'],
                    gpa=data['edu'],
                    hobby=data['hobby']

                )
            )
        await state.finish()
    else:
        db.delete_profile(message.from_user.id)
        async with state.proxy() as data:
            db.sql_insert_profile(
                tg_id=message.from_user.id,
                nickname=data['nickname'],
                bio=data['bio'],
                age=data['age'],
                sign=data['sign'],
                edu=data['edu'],
                hobby=data['hobby'],
                photo=path.name

            )
        await state.finish()
        await bot.send_message(chat_id=message.from_user.id,text="Ur profile succesfully updated")


        await bot.send_message(
            chat_id=message.from_user.id,
            text="U have successfully registered 🎉🍾\n"
                 "Congrats!!!"
        )
    await state.finish()


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_bio,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac_sign,
        state=RegistrationStates.zodiac_sign,
        content_types=['text']
    )
    dp.register_message_handler(
        load_education,
        state=RegistrationStates.education,
        content_types=['text']
    )
    dp.register_message_handler(
        load_hobby,
        state=RegistrationStates.hobby,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )

    dp.register_callback_query_handler(registration_start,lambda call:call.data=='update')