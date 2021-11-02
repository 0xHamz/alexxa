from asyncio import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from cache.admins import set
from helpers.channelmusic import get_chat_id
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command, other_filters
from callsmusic import callsmusic
from callsmusic.queues import queues

from config import UPDATES_CHANNEL
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from pyrogram.errors import FloodWait, UserNotParticipant
from helpers.fsub import handle_force_subscribe

@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text("❗ Tidak Ada Music!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("▶️ Music Dihentikan!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text("❗ Tidak Ada Music!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("⏸ Music Dilanjutkan!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Tidak Ada Music!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("❌ Music Dimatikan!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Tidak Ada Music!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
            await message.reply_text("Music Dihentikan, Tidak Ada Antrian Lagi")
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )
    qeue = que.get(message.chat.id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"**Skip** ke music berikutnya!\nJudul : **{qeue[0][0]}**")

@Client.on_message(filters.command("reload"))
@errors
async def reload(_, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(
                filter="administrators"
            )
        ),
    )

    await message.reply_text("✅️ **Daftar admin** telah **diperbarui**")