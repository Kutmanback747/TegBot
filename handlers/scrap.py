from aiogram import types, Dispatcher
from config import bot
from keyboards import start_inline_buttons
from database import bot_db
from scraping.async_scraper import AsyncScraper


async def Latest_News(call:types.CallbackQuery):
    data=bot_db.Database()
    news=AsyncScraper()
    links= await news.get_page()
    for i in links:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=i
        )
        data.sql_insert_news(link=i,name=call.from_user.first_name,id=call.from_user.id)


def registr_scrap(dp:Dispatcher):
    dp.register_callback_query_handler(Latest_News,lambda call:call.data=='latest_news')

