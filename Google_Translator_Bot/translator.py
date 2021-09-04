from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from Google_Translator_Bot.Language import LANGUAGE
from googletrans import Translator

@Client.on_message(filters.private & filters.text)
async def translator(client, message):

  await message.reply_text("✔️Select your language to translate your text 👇",reply_to_message_id = message.message_id, reply_markup = LANGUAGE)

@Client.on_callback_query()
async def translate_msg(bot,update):
  translator_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = Translator()
  translated = translator.translate(translator_text,lang_tgt=cbdata)
  await update.message.edit(translated.text)
  
