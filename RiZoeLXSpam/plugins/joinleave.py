import os
from telethon import events
from telethon.tl import functions
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from resources.data import *
import re

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
async def join(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n{hl}join <Public Channel or Group Link/Username>"
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = rizoel[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Joined Successfully ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
async def privatejoin(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n{hl}pjoin <Private Group link or access hash>"
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            if bc.startswith("https://t.me/+"):
                hash = bc.split('/t.me/+')[1]
                grp = bc
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(grp))
                await event.edit("Joined Successfully (Private Group/channel) ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in DEV:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            if bc.startswith("https://t.me/") or bc.startswith("@"):
               if re.search(GRP.lower(), bc.lower()):
                   return await e.reply("**Sorry !!** I can't Leave That Group")
               k = await e.client.get_entity(bc)
               id = k.id
            elif bc.startswith("-100"):
                id = int(bc)
                if int(id) in GROUP:
                    return await e.reply("Sorry! I can't Leave This Group")
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
               await event.client(LeaveChannelRequest(id))
               await event.edit("Succesfully Left ✅")
            except Exception as e:
               await event.edit(str(e))
         
        else:
             bc = e.chat_id
             if int(bc) in GROUP:
                text = f"I can't Leave This Grp"
                await e.reply(text, parse_mode=None, link_preview=None )
             else:
                 Xd = int(bc)
                 text = "Leaving....."
                 if e.is_private:
                       dik = f"You Can't Do this Here !! \n\n {hl}leave <chat id or Username> \n {hl}leave : type in the group bot will auto leave that group !"
                       await e.reply(dik, parse_mode=None, link_preview=None )
               
                 else:
                      event = await e.reply(text, parse_mode=None, link_preview=None )
                      try:
                          await event.client(LeaveChannelRequest(Xd))
                      except Exception as e:
                           await event.edit(str(e))
    if e.sender_id in SUDO_USERS:
            await e.reply("Only Full Sudo Users Can Do That Noob !!")
