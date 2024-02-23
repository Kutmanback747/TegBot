import datetime
from aiogram import types, Dispatcher
import database.bot_db
from config import bot, GROUP_ID
from keyboards import questionnaire_inline_buttons
from profanity_check import predict, predict_prob
from const import CHECK_BAN_USER,CHECK_NO_BAN_USER


async def chat_messages(message:types.Message):
    db = database.bot_db.Database()
    if message.chat.id == int(GROUP_ID):
        ban_words_prob = predict_prob([message.text])
        if ban_words_prob > 0.8:
            potential = db.sql_select_ban_user(
                tg_id=message.from_user.id
            )

            print(potential)

            if not potential:
                db.sql_insert_ban_user(
                    tg_id=message.from_user.id
                )
            elif potential['count'] >= 3:
                # await bot.ban_chat_member(
                #     chat_id=message.chat.id,
                #     user_id=message.from_user.id,
                #     until_date=datetime.now()+ datetime.timedelta(hours=1)
                #
                # )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"User:{message.from_user.first_name}banned\n"
                         f"Ban count: {potential['count']}"
                     
                )
            else:
                db.sql_update_ban_count(
                    tg_id=message.from_user.id
                )
            await message.delete()
            await bot.send_message(
                chat_id=message.chat.id,
                text=f'Hello{message.from_user.first_name}\n'
                     f'Dont curse in our chat!!!'
            )

async def check_ban(call:types.CallbackQuery):
    db = database.bot_db.Database()
    user = db.sql_select_ban_user(call.from_user.id)
    if user:
        await call.message.answer(CHECK_BAN_USER.format(
                nickname=call.from_user.full_name,
                count = user['count']
            )
        )
    else:
        await call.message.answer(CHECK_NO_BAN_USER.format(
            nickname=call.from_user.full_name
        ))
def register_group_actions_handlers(dp:Dispatcher):
    dp.register_message_handler(
        chat_messages
    )
    dp.register_callback_query_handler(
        check_ban, lambda call:call.data == 'check'
    )

