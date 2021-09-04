from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from googletrans import Translator
from Google_Translator_Bot.Language import LANGUAGE


@Client.on_message(filters.text & filters.private )
async def echo(client, message):

 
 await  message.reply_text(
                           "Select language 👇",
                           reply_to_message_id = message.message_id,
                           reply_markup = LANGUAGE
                           ) 

    
@Client.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cb_data = update.data
  translator = Translator()  
  translation = translator.translate(tr_text,dest=cb_data) 
  await update.message.edit(translation.text)
