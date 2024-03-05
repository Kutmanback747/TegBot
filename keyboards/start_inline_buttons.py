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
        "View ur penalties",
        callback_data="check"
    )
    my_prof_button = InlineKeyboardButton(
        "View my profile",
        callback_data="my_profile"
    )
    delete_button = InlineKeyboardButton(
        "Delete",
        callback_data="delete"
    )
    update_button = InlineKeyboardButton(
        "Update",
        callback_data="update"
    )

    reference_button = InlineKeyboardButton(
        "Reference",
        callback_data="reference_menu"
    )

    news_button = InlineKeyboardButton(
        "Latest News📰",
        callback_data="latest_news"
    )
    c1_button = InlineKeyboardButton(
        "Advanced level",
        callback_data="advanced"
    )

    b2_button = InlineKeyboardButton(
        "Upp-Intermediate",
        callback_data="upperInt"
    )
    b1_button = InlineKeyboardButton(
        "Inter",
        callback_data="inter"
    )
    a2_button = InlineKeyboardButton(
        "Elementary",
        callback_data="ele"
    )
    a1_button = InlineKeyboardButton(
        "Beginner",
        callback_data="begin"
    )

    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(profiles_button)
    markup.add(check_button)
    markup.add(my_prof_button)
    markup.add(delete_button)
    markup.add(update_button)
    markup.add(reference_button)
    markup.add(news_button)
    markup.add(c1_button)
    markup.add(b2_button)
    markup.add(b1_button)
    markup.add(a2_button)
    markup.add(a1_button)
    return markup


def save(link):
    return None