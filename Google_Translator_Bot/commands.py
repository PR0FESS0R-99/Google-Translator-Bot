from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation

@Client.on_message(filters.private & filters.command("start"))
async def start_main(main, update):
    await update.reply_text(
        text = Translation.START_MSG.format(update.from_user.first_name),
        parse_mode = "markdown",
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text = "Support Group",
                        url="t.me/Mo_Tech_Group"
                    ),
                    InlineKeyboardButton(
                        text = "Open Source",
                        url = "https://github.com/PR0FESS0R-99/Google-Translater-Bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text = "📢 Join Updates Channel 📢" ,
                        url="t.me/Mo_Tech_YT"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.private & filters.command("about"))
async def about_main(main, update):
    await update.reply_text(
        text = Translation.ABOUT_MSG,
        parse_mode = "markdown",
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text = "📢 Join Updates Channel 📢" ,
                        url="t.me/Mo_Tech_YT"
                    )
                ]
            ]
        )
    )