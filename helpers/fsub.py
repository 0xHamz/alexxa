import asyncio
from config import UPDATES_CHANNEL
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_subscribe(bot, message: Message):
    try:
        invite_link = await bot.create_chat_invite_link(int(UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    keyboard = InlineKeyboardMarkup([
                 [ InlineKeyboardButton(
                        "☕ ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/robotprojectx"), 
                 InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ ☕", url=f"https://t.me/justthetech")],
                ])
            
    try:
        userr = await bot.get_chat_member(int(UPDATES_CHANNEL), message.from_user.id)
        if userr.status == "kicked":
            await message.reply(
                reply_markup=keyboard,
                text="**Oops, Kamu Belum Join!**\n\nUntuk Mengurangi Overload, Hanya Subscriber yang dapat menggunakan Bot ini!",
                disable_web_page_preview=True,
            )
            return 400
    except UserNotParticipant:
        await message.reply(
            text="**Oops, Kamu Belum Join!**\n\nUntuk Mengurangi Overload, Hanya Subscriber yang dapat menggunakan Bot ini!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚙️ ᴄʜᴀɴɴᴇʟ", url=invite_link.invite_link)
                    ],
                ]
            ),
        )
        return 400
    except Exception:
        await message.reply(
            text="❌ Error. \n\nContact My [أكبر](https://t.me/justthetech).",
            disable_web_page_preview=True,
        )
        return 400
