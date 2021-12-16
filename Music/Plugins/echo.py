from pyrogram import filters
from pyrogram.types import Message

from Music import app
from Music.MusicUtilities.helpers.decorators import authorized_users_only
from Music.MusicUtilities.helpers.filters import command


@app.on_message(command("s") & filters.group)
@authorized_users_only
async def s(client, message: Message):
    r = message.reply_to_message
    c = message.chat.id
    await message.delete()
    await app.send_sticker(c, r.sticker.file_id)


@app.on_message(command("p") & filters.group)
@authorized_users_only
async def p(client, message: Message):
    replied = message.reply_to_message
    chat_id = message.chat.id
    urlissed = message.text.split(None, 1)[1]
    if replied:
        await message.delete()
        await replied.reply(f"{urlissed}")
        return
    await message.delete()
    await client.send_message(chat_id, f"{urlissed}")
