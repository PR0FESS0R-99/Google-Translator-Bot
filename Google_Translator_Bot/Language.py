from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 

LANGUAGE = InlineKeyboardMarkup([[
InlineKeyboardButton("English", callback_data='en'),
InlineKeyboardButton("മലയാളം", callback_data='ml')
]]
)
