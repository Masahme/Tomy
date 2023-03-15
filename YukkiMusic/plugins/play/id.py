import asyncio
from YukkiMusic import app
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(
    command(["ايدي", "ايديي", "ا"])
    & ~filters.edited
)
async def elkatibk(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    username = f"@{message.from_user.username}"
    bio = (await app.get_chat(message.from_user.id)).bio
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text(       f"""**• اسـمك» ** {message.from_user.mention}\n\n• معـرفـك»  @{message.from_user.username}\n\n• ايـدي » `{message.from_user.id}`\n• الـبايو » {bio}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       name, url=f"https://t.me/{message.from_user.username}")
                ],
                [  
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥⍆", url=f"https://t.me/source_av"),
                ],
            ]
        ),
    )


