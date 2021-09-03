from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command("start"))
async def start_main(main, update):
    await update.reply_text("Hy")
