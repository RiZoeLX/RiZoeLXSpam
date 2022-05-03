
import os
import sys
from telethon.tl import functions, types
from telethon import events, version
from RiZoeLXSpam import (OWNER_ID, StartTime, rizoelversion, ALIVE_PIC, ALIVE_MSG, PING_MSG, HEROKU_API_KEY, HEROKU_APP_NAME)
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError, FloodWaitError, RPCError

def xHell(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    xd = (
        ((str(weeks) + "ᴡ:") if weeks else "")
        + ((str(days) + "ᴅ:") if days else "")
        + ((str(hours) + "ʜ:") if hours else "")
        + ((str(minutes) + "ᴍ:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if xd.endswith(":"):
        return xd[:-1]
    else:
        return xd

pongg = PING_MSG if ALIVE_PIC else "ʀɪᴢᴏᴇʟ X sᴘᴀᴍ"
RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "𝗥𝗶𝗭𝗼𝗲𝗟 𝗫 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲."

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.reply_to_msg_id:
            fuk = await e.respond("Pᴏɴɢ!!.....", reply_to=e.reply_to_msg_id)
        else:
            fuk = await e.reply("Pᴏɴɢ!!.....")  
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        uptime = xHell((time.time() - StartTime) * 1000)
        pingop = f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: {uptime}"
        await fuk.edit(pingop)

rizoel = f"✧ {Alivemsg} ✧\n\n"
rizoel += f"════════════════════\n"
rizoel += f"► **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
rizoel += f"► **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
rizoel += f"► **ʀɪᴢᴏᴇʟXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"  
rizoel += f"► **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/DNHxHELL)\n"
rizoel += f"► **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/RiZoeLX)\n"
rizoel += f"════════════════════\n\n"
rizoel += f"[•Repo•](https://github.com/MrRizoel/RiZoeLXSpam)"            
         
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
   if event.sender_id in SUDO_USERS or event.sender_id in DEV:
     await event.client.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        text = f"**Restarting** \n\n Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Riz.disconnect()
        except Exception:
            pass
        try:
            await Riz2.disconnect()
        except Exception:
            pass
        try:
            await Riz3.disconnect()
        except Exception:
            pass
        try:
            await Riz4.disconnect()
        except Exception:
            pass
        try:
            await Riz5.disconnect()
        except Exception:
            pass
        try:
            await Riz6.disconnect()
        except Exception:
            pass
        try:
            await Riz7.disconnect()
        except Exception:
            pass
        try:
            await Riz8.disconnect()
        except Exception:
            pass
        try:
            await Riz9.disconnect()
        except Exception:
            pass
        try:
            await Riz10.disconnect()
        except Exception:
            pass
        try:
            await Riz11.disconnect()
        except Exception:
            pass
        try:
            await Riz12.disconnect()
        except Exception:
            pass
        try:
            await Riz13.disconnect()
        except Exception:
            pass
        try:
            await Riz14.disconnect()
        except Exception:
            pass
        try:
            await Riz15.disconnect()
        except Exception:
            pass
        try:
            await Riz16.disconnect()
        except Exception:
            pass
        try:
            await Riz17.disconnect()
        except Exception:
            pass
        try:
            await Riz18.disconnect()
        except Exception:
            pass
        try:
            await Riz19.disconnect()
        except Exception:
            pass
        try:
            await Riz20.disconnect()
        except Exception:
            pass
        try:
            await Riz21.disconnect()
        except Exception:
            pass
        try:
            await Riz22.disconnect()
        except Exception:
            pass
        try:
            await Riz23.disconnect()
        except Exception:
            pass
        try:
            await Riz24.disconnect()
        except Exception:
            pass
        try:
            await Riz25.disconnect()
        except Exception:
            pass
        try:
            await Riz26.disconnect()
        except Exception:
            pass
        try:
            await Riz27.disconnect()
        except Exception:
            pass
        try:
            await Riz28.disconnect()
        except Exception:
            pass
        try:
            await Riz29.disconnect()
        except Exception:
            pass
        try:
            await Riz30.disconnect()
        except Exception:
            pass
        try:
            await Riz31.disconnect()
        except Exception:
            pass
        try:
            await Riz32.disconnect()
        except Exception:
            pass
        try:
            await Riz33.disconnect()
        except Exception:
            pass
        try:
            await Riz34.disconnect()
        except Exception:
            pass
        try:
            await Riz35.disconnect()
        except Exception:
            pass
        try:
            await Riz36.disconnect()
        except Exception:
            pass
        try:
            await Riz37.disconnect()
        except Exception:
            pass
        try:
            await Riz38.disconnect()
        except Exception:
            pass
        try:
            await Riz39.disconnect()
        except Exception:
            pass
        try:
            await Riz40.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def bot_help(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        RiZoeL = e.text.split(" ")
        if len(RiZoeL) > 1:
            helping = RiZoeL[1]
            if helping.lower() == "spam":
                await e.reply(spam_help)
            elif helping.lower() == "raid":
                await e.reply(raid_help)
            elif helping.lower() == "dm":
                await e.reply(dm_help)
            elif helping.lower() == "echo":
                await e.reply(echo_help)
            elif helping.lower() == "userbot":
                await e.reply(userbot_help)
            elif helping.lower() == "join":
                await e.reply(join_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "extra":
                await e.reply(extra_help)
            elif helping.lower() == "owner":
                await e.reply(owner_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
**• Spam Cmds •**

**spam**: Spams a message for given counter(<= 100).
commands:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
commands:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
commands:
i) {hl}delayspam <delay time(seconds)> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay time(seconds)> <count> <replying any message>

**pornspam**: Spams hanging message for given counter.
commands:
i) {hl}pornspam <counter>

**packspam**: Spams all stickers from sticker pack.
commands: 
i) {hl}packspam (replying to any sticker)

**hang**: Spams hanging message for given counter.
commands:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

**© @RiZoeLX**
"""


raid_help = f"""
**• Raid Cmds •**

**raid:** Activates raid on any individual user for given range.
commands:
i) {hl}raid <count> <username>
ii) {hl}raid <count> <reply to the user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** Activates reply raid on individual user
commands:
i) {hl}replyraid <replying to anyone>
ii) {hl}replyraid <username>

**dreplyraid:** De-activates reply raid from user!!
commands:
i) {hl}dreplyraid <replying to anyone>
ii) {hl}dreplyraid <username>


**© @RiZoeLX**
"""


dm_help = f"""
**• Dm Cmds •**

**Dm:** Dm to any individual using spam bots
command:
i) {hl}dm <username> <message>
ii) {hl}dm <message> <reply to the user>

**Dm Spam:** Spam in Dm of Any individual Users
command:
i) {hl}dmspam <count> <username> <message to spam>
ii) {hl}dmspam <count> <username> <reply to a message>

**Dm Raid:** raid in Dm of Any individual Users
command:
i) {hl}dmraid <count> <username>
ii) {hl}dmraid <count> <reply to the user>

**© @RiZoeLX**
"""

echo_help = f"""
**• Echo cmds •**

**addecho:** Active Echo On user
Command:
{hl}addecho <reply to user>

**rmecho:** De-activate Echo From user
Command:
{hl}rmecho <reply to user>

**© @RiZoeLX**
"""

join_help = f"""
**• Join Cmds •**

**join:** Join any Public Channel and group
command:
{hl}join <channel/group invite link or username>

**pjoin:** Join Any Private Channel Or group
command:
{hl}pjoin <channel/group Hash>

Example: group Link : https://t.me/+Abcdefghijkl
cmd : {hl}pjoin Abcdefghijkl

__Only Owner And Full Sudo Users can !!__

**© @RiZoeLX
"""

leave_help = f"""
**• Leave Cmds •**

**leave:** Leave any Public/private Group or Channel
commands:
i) {hl}leave <group or channel chat id>
ii) {hl}leave

__Only Owner And Full Sudo Users can !!__

**© @RiZoeLX**
"""

userbot_help = f"""
**• Userbot Cmds •**

**Commands:**

- {hl}ping : To check Ping 

- {hl}alive : To check Bot Version and Other info

- {hl}restart : To Restart Your Spam Bots

**© @RiZoeLX**
"""

extra_help = f"""
**• Extra Cmds •**

**abuse:** Abuse Any Individual user continuously
command:
{hl}abuse <username>

__we'll Add More Cmds Soon__

**© @RiZoeLX**
"""

owner_help = f"""
**• Owner And Full Sudo Cmds •**
__Note__ : Only Spam Bot's Owner and Full Sudo Can Use this cmds.

**Scraping:** members adding In Group
command:
{hl}scrape <Public Group invite Link or username>

**Profile:** Profile And Other Cmds
commands:

1) {hl}setname <Profile Name>
2) {hl}setbio <coustom Bio>
3) {hl}setpic <reply to media>
4) {hl}stats

**Add Sudo:** Add Sudo Using Spam bots
commands:
1) {hl}addsudo <reply to user>
2) {hl}fullsudo <reply to user>
"""

help_menu = f"""
**RiZoeL X Spam Help**

**There are following categories**

`owner` : Get all owner and Full Sudo commands and its usage
`spam` : Get all spam commands and its usage
`raid` : Get all raid commands and its usage
`dm` : Get all dm commands and its usage
`echo` : Get echo commands and its usage
`join` : Get join commands and its usage
`leave` : Get leave commands and its usage
`userbot` : Get all userbot commands
`extra` : Get all extra commands and its usage

**Type** {hl}help <category> **to get all commands in that category and its usage**
**Example**: `{hl}help spam`

**© @RiZoeLX**
"""


import heroku3

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)
full_sudo = os.environ.get("FULLSUDO", None)
        
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID or e.sender_id in DEV:
        ok = await event.reply("Adding user as a sudo...")
        rizoel = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user 🔱 Restarting.. Please wait a minute...")
        heroku_var[rizoel] = newsudo

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sfullsudo(?: |$)(.*)" % hl))
async def fs(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        rizoel = "FULLSUDO"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if full_sudo:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a full sudo user 🔱 Restarting.. Please wait a minute...")
        heroku_var[rizoel] = newsudo

    if event.sender_id in DEV:
        await event.reply("Only Owner Can Add Full Sudo You Can add Sudo Users Only.")

# Scrape

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
async def get_users(event):
    if event.sender_id == OWNER_ID or event.sender_id in DEV:
        fukyou = event.text.split(" ", 1)
        group = fukyou[1]
        if group.startswith("https://t.me/") or group.startswith("@"):
             await event.client(functions.channels.JoinChannelRequest(group))
             peer = 0
             a = 0
             Add_Msg = await event.client.send_message(event.chat_id, f"__️Scraping Users From: {group}__")
             async for sex in event.client.iter_participants(group, aggressive=True):
             #   await Add_Msg.edit(f"**• Scraping Users •** \n\n • __From Chat:__ {group} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
                try:
                   await event.client(InviteToChannelRequest(event.chat_id, [sex]))
                   await asyncio.sleep(3)
                   a += 1
                except FloodWaitError as s:
                #   await Add_Msg.edit(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Users Added:** `{a}` \n **Scrape Group**: `{group}`")
                   return
                except UserPrivacyRestrictedError:
                   print("PrivacyRestrictedError")
                except UserAlreadyParticipantError:
                   print("User Already In Group")
                except UserBannedInChannelError:
                   print("User Banned in Group")
                except ChatAdminRequiredError:
                   print("Error: To Add Members Chat Admin Required")
                 #  await Add_Msg.edit(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                   return
                except ValueError:
                   print(f"Error: Can't Find Group/channel")
                #   await Add_Msg.edit(f"**Error 204 !!** \n Can't Find Group/Channel")
                   return
                except PeerFloodError:
                 if peer == 10:
                    print("PeerFloodError")
                    peer += 1  
                   # await Add_Msg.edit(f"**Error 102 !!** \n PeerFloodError !")
                    return
                except RPCError as ok:
                   print(f"ok.__class__.__name__")
                except Exception as e:
                   print(e)
             return await Add_Msg.edit(f"**• Users Added •** \n\n • __From Chat:__ {group} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")