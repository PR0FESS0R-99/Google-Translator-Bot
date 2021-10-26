import os, asyncio, aiofiles, aiofiles.os, datetime, traceback,random, string, time, logging
logger = logging.getLogger(__name__)
from random import choice
from Google_Translator_Bot.Database import Database
from pyrogram import filters
from pyrogram import Client as google_transletor_bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Google_Translator_Bot.Language import BOT_LANGUAGE, GROUP_LANGUAGE
from translation import Translation
from googletrans import Translator
from config import Config

db = Database()

@google_transletor_bot.on_message(filters.private & filters.command("start"))
async def start_main(main, update):
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)  
    await update.reply_text(
        text = Translation.START_MSG.format(update.from_user.first_name),
        parse_mode = "markdown",
        reply_markup = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton
                        (
                            text = "✅️ Deploy Now ✅️", url = "https://github.com/PR0FESS0R-99/Google-Translator-Bot"
                         )
                ],
                [
                    InlineKeyboardButton
                        (
                            text = "🤠 Credits 🤠", callback_data="credits"
                        )
                ]
            ]
        )
    )

@google_transletor_bot.on_message(filters.command("tr"))
async def echo(client, message): 
    await message.reply_text(
        Translation.TRANSLATED_MSG,
        reply_markup = GROUP_LANGUAGE,
        quote = True
    )

@google_transletor_bot.on_message(filters.private & filters.text & ~filters.command(["start", "broadcast"]))
async def echo(client, message): 
    await message.reply_text(
        Translation.TRANSLATED_MSG,
        reply_markup = BOT_LANGUAGE,
        quote = True
    )

broadcast_ids = {}

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"

@google_transletor_bot.on_message(filters.private & filters.command("broadcast") & filters.reply)
async def broadcast_(c, m):
    print("broadcasting......")
    if m.from_user.id not in Config.DEV_ID:
        await c.delete_messages(
            chat_id=m.chat.id,
            message_ids=m.message_id,
            revoke=True
        )
        return
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    
    out = await m.reply_text(
        text = f"Broadcast initiated! You will be notified with log file when all the users are notified."
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    
    broadcast_ids[broadcast_id] = dict(
        total = total_users,
        current = done,
        failed = failed,
        success = success
    )
    
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            
            sts, msg = await send_msg(
                user_id = int(user['id']),
                message = broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            
            if sts == 200:
                success += 1
            else:
                failed += 1
            
            if sts == 400:
                await db.delete_user(user['id'])
            
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current = done,
                        failed = failed,
                        success = success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
    
    await asyncio.sleep(3)
    
    await out.delete()
    
    if failed == 0:
        await m.reply_text(
            text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"""broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.""",
            quote=True
        )
    
    await aiofiles.os.remove('broadcast.txt')



