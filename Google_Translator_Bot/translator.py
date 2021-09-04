from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from Google_Translator_Bot.Language import LANGUAGE
from google_trans_new import google_translator

@Client.on_message(filters.private & filters.text)
def translation(client, message):
  message.reply_text("✔️Select your language to translate your text 👇",reply_to_message_id = message.message_id, reply_markup = LANGUAGE)

@Client.on_callback_query()
async def translate_msg(bot,update):
  translator_text = update.message.reply_to_message.text
  cb_data = update.data
  translator = google_translator()
  translator_msg = translator.translate(translator_text,lang_tgt=cb_data)
  await update.message.edit(translator_msg)
  
