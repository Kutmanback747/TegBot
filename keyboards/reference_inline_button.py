from aiogram.types import (
    InlineKeyboardButton,

    InlineKeyboardMarkup
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Generate_link",
        callback_data="reference_link"
    )

    list_button = InlineKeyboardButton(
        "Generate_list",
        callback_data="reference_list"
    )

    markup.add(link_button),
    markup.add(list_button)
    return markup
