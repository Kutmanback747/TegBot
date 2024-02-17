from aiogram import types, Dispatcher
from config import bot
from keyboards import questionnaire_inline_buttons


async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Messi 🧑‍🦱or Ronaldo👨‍🦱  ?",
        reply_markup=await questionnaire_inline_buttons.questionnaire_keyboard()
    )



async def messi_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh,no it's too incredible"
             "Do u want switch to another soccer ?",
        reply_markup=await questionnaire_inline_buttons.messi_questionnaire_keyboard()
    )

async def ronaldo_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh,it's good i'm too fan of Ronaldo",

        reply_markup=await questionnaire_inline_buttons.ronaldo_questionnaire_keyboard()
    )


async def yes_messi_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Ronaldo is better than Messi")



async def no_messi_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool i'm fan Ronaldo too")


async def yes_ronaldo_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="oh'cool ")



async def no_ronaldo_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="oh ")

def register_questionnaire_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        messi_answer,
        lambda call:call.data == "messi"
    )
    dp.register_callback_query_handler(
        ronaldo_answer,
        lambda call:call.data == "ronaldo"
    )

    dp.register_callback_query_handler(
        yes_messi_answer,
        lambda call: call.data == "yes_messi"
    )
    dp.register_callback_query_handler(
        no_messi_answer,
        lambda call: call.data == "no_messi"
    )
    dp.register_callback_query_handler(
        yes_ronaldo_answer,
        lambda call: call.data == "yes_ronaldo"
    )
    dp.register_callback_query_handler(
        no_ronaldo_answer,
        lambda call: call.data == "no_ronaldo"
    )




