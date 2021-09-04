from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from googletrans import Translator
from Google_Translator_Bot.Language import LANGUAGE


@Client.on_message(filters.text & filters.private )
async def echo(client, message):
 
 keybord = InlineKeyboardMarkup( [
        [
            InlineKeyboardButton("Hindi", callback_data='hi'),
            InlineKeyboardButton("Kannada", callback_data='kn'),
            InlineKeyboardButton("malayalam",callback_data ='ml')
        ],
        [   InlineKeyboardButton("Tamil", callback_data='ta'),
        InlineKeyboardButton("Telugu", callback_data='te'),
        InlineKeyboardButton("English",callback_data = 'en')
        ],
        	[InlineKeyboardButton("Urdu",callback_data ="ur"),
	InlineKeyboardButton("Punjabi",callback_data="pa"),
	InlineKeyboardButton("Spanish",callback_data="es")
	]
    ]
 
 )

 
 await  message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup = keybord1) 

    
@app.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cb_data = update.data
  if cb_data== "page":
  	await update.message.edit("Select language 👇",reply_markup = keybord)
  elif cb_data == "page1":
        await update.message.edit("Select language 👇",reply_markup = LANGUAGE)
  else :
       translator = Translator()  
       translation = translator.translate(tr_text,dest=cb_data) 
       await update.message.edit(translation.text)
