from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/439b2b1029e1d3e748fa7.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 𝐕𝐈𝐏 𝐁𝐎𝐘 🌹", url=f"@GOVIND_OFFICIAL_MP42")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 GOVIND 🌹", url=f"@GOVIND_OFFICIAL_MP42")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("Govind")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/439b2b1029e1d3e748fa7.jpg",
        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀
👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "【🇬𝐎𝐕𝐈𝐍𝐃 𒆜 🇻𝐀𝐑𝐌𝐀】", url=f"@GOVIND_OFFICIAL_MP42")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("natakhat_pari")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/439b2b1029e1d3e748fa7.jpg",
        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀
👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "【🇬𝐎𝐕𝐈𝐍𝐃 𒆜 🇻𝐀𝐑𝐌𝐀】", url=f"@GOVIND_OFFICIAL_MP42")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/439b2b1029e1d3e748fa7.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

