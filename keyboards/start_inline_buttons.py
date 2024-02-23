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

    registration_button = InlineKeyboardButton(
        "Registration🪪",
        callback_data="registration"
    )
    profiles_button = InlineKeyboardButton(
        "View Profiles",
        callback_data="random_profiles"
    )
    check_button = InlineKeyboardButton(
        "Viev ur penalties",
        callback_data="check"
    )

    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(profiles_button)
    markup.add(check_button)
    return markup
