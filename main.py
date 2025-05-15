import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import config as cnfg
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    photo = types.FSInputFile("images/crackdonalds.png")
    await bot.send_photo(message.chat.id, photo = photo, caption =cnfg.main_menu_text, reply_markup = cnfg.main_menu_markup.as_markup(), parse_mode="HTML")

@dp.callback_query(F.data == "general")
async def cmd_price(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=cnfg.general_info_text, parse_mode = 'HTML', reply_markup = cnfg.back_markup.as_markup())

@dp.callback_query(F.data == "roadmap")
async def cmd_price(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=cnfg.roadmap_text, parse_mode = 'HTML', reply_markup = cnfg.back_markup.as_markup())

@dp.callback_query(F.data == "whale")
async def cmd_price(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=cnfg.whale_text, parse_mode = 'HTML', reply_markup = cnfg.back_markup.as_markup())

@dp.callback_query(F.data == "links")
async def cmd_price(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=cnfg.links_text, parse_mode = 'HTML', reply_markup = cnfg.back_markup.as_markup())

@dp.callback_query(F.data == "chart")
async def cmd_price(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=cnfg.charts_text, parse_mode = 'HTML', reply_markup = cnfg.back_markup.as_markup())

@dp.callback_query(F.data == "airdrop")
async def cmd_price(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=cnfg.airdrop_text, parse_mode = 'HTML', reply_markup = cnfg.back_markup.as_markup())

@dp.callback_query(F.data == "nft")
async def cmd_price(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=cnfg.nft_text, parse_mode = 'HTML', reply_markup = cnfg.back_markup.as_markup())

@dp.callback_query(F.data == "back")
async def cmd_back(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=cnfg.main_menu_text, parse_mode="HTML", reply_markup=cnfg.main_menu_markup.as_markup())

async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())