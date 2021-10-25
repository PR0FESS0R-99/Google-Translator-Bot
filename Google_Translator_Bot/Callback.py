from pyrogram import filters
from pyrogram import Client as google_transletor_bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from googletrans import Translator
from Google_Translator_Bot.Language import BOT_LANGUAGE
from translation import Translation

@google_transletor_bot.on_callback_query(filters.regex('^languages$'))
async def back_to_langs(bot, update):
    await update.edit_message_text(
        Translation.TRANSLATED_MSG,
        reply_markup = BOT_LANGUAGE
    )

@google_transletor_bot.on_callback_query(filters.regex('^lang .+$'))
async def translate_text(bot,update):
    try:
        translation_text = update.message.reply_to_message.text
    except AttributeError:
        await update.answer('Input Not Found', True)
        return await update.message.delete()
    
    cb_data = update.data
    lang_code = cb_data.split(" ", 1)[1]
    translator = Translator()  
    translation = translator.translate(translation_text,dest=lang_code)
    
    await update.edit_message_text(
        text = f"<code>{translation.text}</code>",
        parse_mode = 'html',
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton
                        (
                            text = '🔙 Back to Language List', callback_data = 'languages'
                        )
                ],
                [
                    InlineKeyboardButton
                        (
                            text = '❎️ Close ❎️', callback_data = 'trdelete'
                        )
                ]
            ]
        )
    )

@google_transletor_bot.on_callback_query()
async def callback(client, query_callback):
    if query_callback.data == "trdelete":
       await query_callback.message.delete()
    elif query_callback.data == "credits":
       await query_callback.message.edit_text(Translation.CREDITS, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("Muhammed RK", url="https://github.com/PR0FESS0R-99") ],[ InlineKeyboardButton("Shahsad-klr", url="https://github.com/shahsad-klr") ],[ InlineKeyboardButton("Lntechnical2", url="https://github.com/lntechnical2") ]] ))   
