#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>JINTO NS</a>\n\n○ Language : <a href='https://www.python.org/'>Python3</a>\n\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n\n○ Channel : <a href='https://t.me/jns_bots'>JNS BOTS</a>\n\n○ Support Group : <a href='https://t.me/jns_FC_bots'>BOT DISCUSSION</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🎊ᴊᴏɪɴ ɴᴏᴡ🎉", url=f"https://t.me/jns_bots"),
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
           pass
