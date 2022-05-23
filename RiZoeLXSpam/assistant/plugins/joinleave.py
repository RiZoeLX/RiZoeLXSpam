import os 
import asyncio
from telethon import events
from datetime import datetime
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from resources.data import GROUP, GRP

@RiZoeL.on(events.NewMessage(pattern="[!/]join"))
async def join(event):
  if event.sender_id in DEV or event.sender_id in SUDO_USERS:
     if event.is_group:
          return await event.reply("**Use this Cmd in PM !!**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message("**Send Group Link or Username To Join**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        grpp = res.message.message
        if grpp.startswith("https://t.me/") or grpp.startswith("@"):
            Group = grpp
        else:
            await rizx.send_message("Error! Send Group link or Username")
            return
        hehe = await rizx.send_message("__joining__ .....")
        await asyncio.sleep(1)
        await hehe.edit(f"**Joined Successfully** ✅ \n\n __Group/channel:__ {Group}")
        try:
           if Riz:
                 await Riz(functions.channels.JoinChannelRequest(channel=Group))
           if Riz2:
                 await Riz2(functions.channels.JoinChannelRequest(channel=Group))
           if Riz3:
                 await Riz3(functions.channels.JoinChannelRequest(channel=Group))
           if Riz4:
                 await Riz4(functions.channels.JoinChannelRequest(channel=Group))
           if Riz5:
                 await Riz5(functions.channels.JoinChannelRequest(channel=Group))
           if Riz6:
                 await Riz6(functions.channels.JoinChannelRequest(channel=Group))
           if Riz7:
                 await Riz7(functions.channels.JoinChannelRequest(channel=Group))
           if Riz8:
                 await Riz8(functions.channels.JoinChannelRequest(channel=Group))
           if Riz9:
                 await Riz9(functions.channels.JoinChannelRequest(channel=Group))
           if Riz10:
                 await Riz10(functions.channels.JoinChannelRequest(channel=Group))
           if Riz11:
                 await Riz11(functions.channels.JoinChannelRequest(channel=Group))
           if Riz12:
                 await Riz12(functions.channels.JoinChannelRequest(channel=Group))
           if Riz13:
                 await Riz13(functions.channels.JoinChannelRequest(channel=Group))
           if Riz14:
                 await Riz14(functions.channels.JoinChannelRequest(channel=Group))
           if Riz15:
                 await Riz15(functions.channels.JoinChannelRequest(channel=Group))
           if Riz16:
                 await Riz16(functions.channels.JoinChannelRequest(channel=Group))
           if Riz17:
                 await Riz17(functions.channels.JoinChannelRequest(channel=Group))
           if Riz18:
                 await Riz18(functions.channels.JoinChannelRequest(channel=Group))
           if Riz19:
                 await Riz19(functions.channels.JoinChannelRequest(channel=Group))
           if Riz20:
                 await Riz20(functions.channels.JoinChannelRequest(channel=Group))
           if Riz21:
                 await Riz21(functions.channels.JoinChannelRequest(channel=Group))
           if Riz22:
                 await Riz22(functions.channels.JoinChannelRequest(channel=Group))
           if Riz23:
                 await Riz23(functions.channels.JoinChannelRequest(channel=Group))
           if Riz24:
                 await Riz24(functions.channels.JoinChannelRequest(channel=Group))
           if Riz25:
                 await Riz25(functions.channels.JoinChannelRequest(channel=Group))
           if Riz26:
                 await Riz26(functions.channels.JoinChannelRequest(channel=Group))
           if Riz27:
                 await Riz27(functions.channels.JoinChannelRequest(channel=Group))
           if Riz28:
                 await Riz28(functions.channels.JoinChannelRequest(channel=Group))
           if Riz29:
                 await Riz29(functions.channels.JoinChannelRequest(channel=Group))
           if Riz30:
                 await Riz30(functions.channels.JoinChannelRequest(channel=Group))
           if Riz31:
                 await Riz31(functions.channels.JoinChannelRequest(channel=Group))
           if Riz32:
                 await Riz32(functions.channels.JoinChannelRequest(channel=Group))
           if Riz33:
                 await Riz33(functions.channels.JoinChannelRequest(channel=Group))
           if Riz34:
                 await Riz34(functions.channels.JoinChannelRequest(channel=Group))
           if Riz35:
                 await Riz35(functions.channels.JoinChannelRequest(channel=Group))
           if Riz36:
                 await Riz36(functions.channels.JoinChannelRequest(channel=Group))
           if Riz37:
                 await Riz37(functions.channels.JoinChannelRequest(channel=Group))
           if Riz38:
                 await Riz38(functions.channels.JoinChannelRequest(channel=Group))
           if Riz39:
                 await Riz39(functions.channels.JoinChannelRequest(channel=Group))
           if Riz40:
                 await Riz40(functions.channels.JoinChannelRequest(channel=Group))
        except Exception as ex:
                print(ex)
                
@RiZoeL.on(events.NewMessage(pattern="[!/]pjoin"))
async def pjoin(event):
  if event.sender_id in DEV or event.sender_id in SUDO_USERS:
     if event.is_group:
          return await event.reply("**Use this Cmd in PM !!**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message("**Send Private Group Link or Access hash To Join**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        grpp = res.message.message
        if grpp.startswith("https://t.me/+"):
            hash = grpp.split('/t.me/+')[1]
            Group = grpp
        elif grpp.startswith("+"):
            hash = grpp.split('+')[1]
            Group = "https://t.me/" + grpp
        else:
            await rizx.send_message("Error! Send Private Group link or Hash with '+' \n\n Example: **https://t.me/+FTQryVyYCXshdka* or **+FTQryVyYCXs1YzGsJl**")
            return
        hehe = await rizx.send_message("__joining__ .....")
        await asyncio.sleep(1)
        await hehe.edit(f"**Joined Successfully** ✅ \n\n __Private Group/channel:__ {Group}")
        try:
           if Riz:
                 await Riz(ImportChatInviteRequest(hash))
           if Riz2:
                 await Riz2(ImportChatInviteRequest(hash))
           if Riz3:
                 await Riz3(ImportChatInviteRequest(hash))
           if Riz4:
                 await Riz4(ImportChatInviteRequest(hash))
           if Riz5:
                 await Riz5(ImportChatInviteRequest(hash))
           if Riz6:
                 await Riz6(ImportChatInviteRequest(hash))
           if Riz7:
                 await Riz7(ImportChatInviteRequest(hash))
           if Riz8:
                 await Riz8(ImportChatInviteRequest(hash))
           if Riz9:
                 await Riz9(ImportChatInviteRequest(hash))
           if Riz10:
                 await Riz10(ImportChatInviteRequest(hash))
           if Riz11:
                 await Riz11(ImportChatInviteRequest(hash))
           if Riz12:
                 await Riz12(ImportChatInviteRequest(hash))
           if Riz13:
                 await Riz13(ImportChatInviteRequest(hash))
           if Riz14:
                 await Riz14(ImportChatInviteRequest(hash))
           if Riz15:
                 await Riz15(ImportChatInviteRequest(hash))
           if Riz16:
                 await Riz16(ImportChatInviteRequest(hash))
           if Riz17:
                 await Riz17(ImportChatInviteRequest(hash))
           if Riz18:
                 await Riz18(ImportChatInviteRequest(hash))
           if Riz19:
                 await Riz19(ImportChatInviteRequest(hash))
           if Riz20:
                 await Riz20(ImportChatInviteRequest(hash))
           if Riz21:
                 await Riz21(ImportChatInviteRequest(hash))
           if Riz22:
                 await Riz22(ImportChatInviteRequest(hash))
           if Riz23:
                 await Riz23(ImportChatInviteRequest(hash))
           if Riz24:
                 await Riz24(ImportChatInviteRequest(hash))
           if Riz25:
                 await Riz25(ImportChatInviteRequest(hash))
           if Riz26:
                 await Riz26(ImportChatInviteRequest(hash))
           if Riz27:
                 await Riz27(ImportChatInviteRequest(hash))
           if Riz28:
                 await Riz28(ImportChatInviteRequest(hash))
           if Riz29:
                 await Riz29(ImportChatInviteRequest(hash))
           if Riz30:
                 await Riz30(ImportChatInviteRequest(hash))
           if Riz31:
                 await Riz31(ImportChatInviteRequest(hash))
           if Riz32:
                 await Riz32(ImportChatInviteRequest(hash))
           if Riz33:
                 await Riz33(ImportChatInviteRequest(hash))
           if Riz34:
                 await Riz34(ImportChatInviteRequest(hash))
           if Riz35:
                 await Riz35(ImportChatInviteRequest(hash))
           if Riz36:
                 await Riz36(ImportChatInviteRequest(hash))
           if Riz37:
                 await Riz37(ImportChatInviteRequest(hash))
           if Riz38:
                 await Riz38(ImportChatInviteRequest(hash))
           if Riz39:
                 await Riz39(ImportChatInviteRequest(hash))
           if Riz40:
                 await Riz40(ImportChatInviteRequest(hash))
        except Exception as ex:
                print(ex)

@RiZoeL.on(events.NewMessage(pattern="[!/]leave"))
async def leave(event):
  if event.sender_id in DEV:
     if event.is_group:
          return await event.reply("**Use this Cmd in PM !!**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message("**Send Group Link or Group Id To Leave**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        grpp = res.message.message
        if grpp.startswith("https://t.me/") or grpp.startswith("@"):
              if grpp in GRP:
                  return await rizx.send_message("I can't Leave That Group!!")
              k = await Riz.get_entity(grpp)
              id = k.id
              if int(id) in GROUP:
                 return await rizx.send_message("I can't Leave that Group")
        elif grpp.startswith("-100"):
            if int(grpp) in GROUP:
                return await rizx.send_message("I can't Leave that Group")
            id = grpp
        else:
            await rizx.send_message("**Send Group Link/Username or group id to leave**")
        hehe = await rizx.send_message("__leaving__ .....")
        await asyncio.sleep(1)
        await hehe.edit(f"**Successfully Left** ✅ \n\n __Group ID:__ {id}")
        try:
           if Riz:
                 await Riz(LeaveChannelRequest(id))
           if Riz2:
                 await Riz2(LeaveChannelRequest(id))
           if Riz3:
                 await Riz3(LeaveChannelRequest(id))
           if Riz4:
                 await Riz4(LeaveChannelRequest(id))
           if Riz5:
                 await Riz5(LeaveChannelRequest(id))
           if Riz6:
                 await Riz6(LeaveChannelRequest(id))
           if Riz7:
                 await Riz7(LeaveChannelRequest(id))
           if Riz8:
                 await Riz8(LeaveChannelRequest(id))
           if Riz9:
                 await Riz9(LeaveChannelRequest(id))
           if Riz10:
                 await Riz10(LeaveChannelRequest(id))
           if Riz11:
                 await Riz11(LeaveChannelRequest(id))
           if Riz12:
                 await Riz12(LeaveChannelRequest(id))
           if Riz13:
                 await Riz13(LeaveChannelRequest(id))
           if Riz14:
                 await Riz14(LeaveChannelRequest(id))
           if Riz15:
                 await Riz15(LeaveChannelRequest(id))
           if Riz16:
                 await Riz16(LeaveChannelRequest(id))
           if Riz17:
                 await Riz17(LeaveChannelRequest(id))
           if Riz18:
                 await Riz18(LeaveChannelRequest(id))
           if Riz19:
                 await Riz19(LeaveChannelRequest(id))
           if Riz20:
                 await Riz20(LeaveChannelRequest(id))
           if Riz21:
                 await Riz21(LeaveChannelRequest(id))
           if Riz22:
                 await Riz22(LeaveChannelRequest(id))
           if Riz23:
                 await Riz23(LeaveChannelRequest(id))
           if Riz24:
                 await Riz24(LeaveChannelRequest(id))
           if Riz25:
                 await Riz25(LeaveChannelRequest(id))
           if Riz26:
                 await Riz26(LeaveChannelRequest(id))
           if Riz27:
                 await Riz27(LeaveChannelRequest(id))
           if Riz28:
                 await Riz28(LeaveChannelRequest(id))
           if Riz29:
                 await Riz29(LeaveChannelRequest(id))
           if Riz30:
                 await Riz30(LeaveChannelRequest(id))
           if Riz31:
                 await Riz31(LeaveChannelRequest(id))
           if Riz32:
                 await Riz32(LeaveChannelRequest(id))
           if Riz33:
                 await Riz33(LeaveChannelRequest(id))
           if Riz34:
                 await Riz34(LeaveChannelRequest(id))
           if Riz35:
                 await Riz35(LeaveChannelRequest(id))
           if Riz36:
                 await Riz36(LeaveChannelRequest(id))
           if Riz37:
                 await Riz37(LeaveChannelRequest(id))
           if Riz38:
                 await Riz38(LeaveChannelRequest(id))
           if Riz39:
                 await Riz39(LeaveChannelRequest(id))
           if Riz40:
                 await Riz40(LeaveChannelRequest(id))
        except Exception as ex:
                print(ex)
                
                                
               
