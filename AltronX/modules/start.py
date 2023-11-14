from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("☆ 𝐂σммαиԃ𝐒 ☆", data="help_back")
        ],
        [
        Button.url("☆ 𝐂нαииє𝐋 ☆", "https://t.me/zordangaming"),
        Button.url("☆ 𝐒υρρσя𝐓", "https://t.me/billaganghh")
        ],
        [
        Button.url("☆ 𝐑ꫀρ𝐎", "https://t.me/billaganghh")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝐇𝐞𝐲 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝐈 𝐀𝐦 [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐃 𝐁𝐘 :~ [𝑾𝑬𝑬𝑫𝑳𝑬𝑨𝑭](https://t.me/gamingggggg3)**\n\n"
        TEXT += f"» **𝐎𝐏 𝐒𝐏𝐀𝐌 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :** `3.2`\n"
        TEXT += f"» **𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://te.legra.ph/file/cce5f7d6621faf465ac65.jpg",
                caption=TEXT, 
                buttons=PythonButton)
