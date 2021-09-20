from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from googletrans import Translator
from Google_Translator_Bot.Language import LANGUAGE
from translation import Translation

@Client.on_message(filters.text & filters.private )
async def echo(client, message): 
    await message.reply_text(
        Translation.TRANSLATED_MSG,
        reply_markup = LANGUAGE,
        quote = True
    )

@Client.on_callback_query(filters.regex('^languages$'))
async def back_to_langs(bot, update):
    await update.edit_message_text(
        Translation.TRANSLATED_MSG,
        reply_markup = LANGUAGE
    )

@Client.on_callback_query(filters.regex('^lang .+$'))
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
                    InlineKeyboardButton(
                        text = '🔙 Back to Language List',
                        callback_data = 'languages'
                    )
                ]
            ]
        )
    )
