from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from Google_Translator_Bot.Language import LANGUAGE
from google_trans_new import google_translator

@Client.on_message(filters.private & filters.text)
async def translator(client, msg):
  
msg.reply_text(
"Select Your language 👇",
reply_to_message_id = msg.message_id,
reply_markup = LANGUAGE
)

@Client.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = google_translator()
  translated_text = translator.translate(tr_text,lang_tgt=cbdata)
  await update.message.edit(translated_text)
