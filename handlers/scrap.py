from aiogram import types, Dispatcher
from config import bot
from keyboards import start_inline_buttons
from database import bot_db
from scraping.async_scraper import AsyncEnglishScrapper


async def english_adv(call: types.CallbackQuery):
    datab = bot_db.Database()
    scrapper = AsyncEnglishScrapper()
    links = await scrapper.get_page()
    for link in links[0][:5]:
        datab.insert_eng_table(link=link)
        await bot.send_message(chat_id=call.from_user.id, text=link, reply_markup=await start_inline_buttons.save(link))


async def english_b2(call: types.CallbackQuery):
    datab = bot_db.Database()
    scrapper = AsyncEnglishScrapper()
    links = await scrapper.get_page()
    for link in links[1][:5]:
        datab.insert_eng_table_b2(link=link)
        await bot.send_message(chat_id=call.from_user.id, text=link, reply_markup=await start_inline_buttons.save(link))


async def english_b1(call: types.CallbackQuery):
    datab = bot_db.Database()
    scrapper = AsyncEnglishScrapper()
    links = await scrapper.get_page()
    for link in links[2][:5]:
        datab.insert_eng_table_b1(link=link)
        await bot.send_message(chat_id=call.from_user.id, text=link, reply_markup=await start_inline_buttons.save(link))


async def english_a2(call: types.CallbackQuery):
    datab = bot_db.Database()
    scrapper = AsyncEnglishScrapper()
    links = await scrapper.get_page()
    for link in links[3][:5]:
        datab.insert_eng_table_a2(link=link)
        await bot.send_message(chat_id=call.from_user.id, text=link, reply_markup=await start_inline_buttons.save(link))


async def english_a1(call: types.CallbackQuery):
    datab = bot_db.Database()
    scrapper = AsyncEnglishScrapper()
    links = await scrapper.get_page()
    for link in links[4][:5]:
        datab.insert_eng_table_a1(link=link)
        await bot.send_message(chat_id=call.from_user.id, text=link, reply_markup=await start_inline_buttons.save(link))


async def eng_favourite_save(call: types.CallbackQuery):
    print(';;;')
    datab = bot_db.Database()
    check = datab.select_id_fav_table(tg_id=call.from_user.id, link=call.data[5:])
    if check is None:
        datab.insert_favo_eng_table(
            tg_id=call.from_user.id,
            link=call.data[5:]
        )


def register_scrap(dp: Dispatcher):
    dp.register_callback_query_handler(english_adv, lambda call: call.data == 'advanced')
    dp.register_callback_query_handler(eng_favourite_save, lambda call: call.data.startswith('save'))
    dp.register_callback_query_handler(english_b2, lambda call: call.data == 'upperInt')
    dp.register_callback_query_handler(english_b1, lambda call: call.data == 'inter')
    dp.register_callback_query_handler(english_a2, lambda call: call.data == 'ele')
    dp.register_callback_query_handler(english_a1, lambda call: call.data == 'begin')


def register_scrap_handlers(dp):
    return None