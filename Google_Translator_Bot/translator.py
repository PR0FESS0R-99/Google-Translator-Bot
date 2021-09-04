from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from Google_Translator_Bot.Language import LANGUAGE
from googletrans import Translator

@Client.on_message(filters.private & filters.text)
async def translator(client, message):
  translator_text = update.message.reply_to_message.text
  cb_data = update.data
  if cb_data== "page":
  	await update.message.edit("Select language 👇",reply_markup = LANGUAGE)   
  else :
       translator = Translator()
       translated_msg = translator.translate(translator_text,lang_tgt=cbdata)
       await update.message.edit(translated_msg)
  
