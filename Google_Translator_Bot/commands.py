from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command("start"))
async def start_main(main, update):
    await update.reply_text("Hy")


@Client.on_message(filters.private & filters.text)
async def translator(client, msg):
  
msg.reply_text(
"Select Your language 👇",
reply_to_message_id = msg.message_id,
reply_markup = LANGUAGE
)

