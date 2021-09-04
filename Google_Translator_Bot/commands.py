from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation

@Client.on_message(filters.private & filters.command("start"))
async def start_main(main, update):
    await update.reply_text(Translation.START_MSG.format(update.from_user.mention),
                            reply_to_message_id = update.message_id,
                            parse_mode="markdown",
                            reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("📢 Join Updates Channel 📢" ,url="t.me/Mo_Tech_YT")
                            ]])
                            ) 
                  



  	
