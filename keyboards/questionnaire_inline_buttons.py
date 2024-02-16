from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    messi_button = InlineKeyboardButton(
        "Messi 🧑‍🦱",
        callback_data="messi"
    )
    ronaldo_button = InlineKeyboardButton(
        "Ronaldo 👨‍🦱",
        callback_data="ronaldo"
    )
    markup.add(messi_button)
    markup.add(ronaldo_button)
    return markup

async def messi_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    messi_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_messi"
    )

    messi_no_button =InlineKeyboardButton(
        "No",
        callback_data="no_messi"
    )
    markup.add(messi_button)
    markup.add(messi_no_button)
    return markup

async def ronaldo_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    ronaldo_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_ronaldo"
    )

    ronaldo_no_button =InlineKeyboardButton(
        "No",
        callback_data="no_ronaldo"
    )
    markup.add(ronaldo_button)
    markup.add(ronaldo_no_button)
    return markup