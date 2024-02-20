from aiogram.types import (
    InlineKeyboardButton,

    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"
    )


    registation_button = InlineKeyboardButton(
        "Registration🪪",
        callback_data="registration"
    )
    markup.add(questionnaire_button)
    markup.add(registation_button)
    return markup

