import asyncio
import os
from telethon.tl import functions
from telethon import events
from telethon.tl.functions.photos import UploadProfilePhotoRequest

ABORT = "**All process Cancelled !**"

@RiZoeL.on(events.NewMessage(pattern="[!/]setname"))
async def set_name(event):
  if event.sender_id in DEV:
     if event.is_group:
          return await event.reply("**Use this Cmd in PM !!**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message("**Send New Name to Change The Name**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        name = res.message.message
        ids = 0
        hehe = await rizx.send_message("__Changing name..__")
        await asyncio.sleep(2)
        await hehe.edit(f"**Name Changed Successfully ✅** \n\n **New Name:** {name}")
        try:
           if Riz:
                 await Riz(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz2:
                 await Riz2(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz3:
                 await Riz3(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz4:
                 await Riz4(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz5:
                 await Riz5(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz6:
                 await Riz6(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz7:
                 await Riz7(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz8:
                 await Riz8(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz9:
                 await Riz9(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz10:
                 await Riz10(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz11:
                 await Riz11(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz12:
                 await Riz12(functions.account.UpdateProfileRequest(first_name=name)) 
           if Riz13:
                 await Riz13(functions.account.UpdateProfileRequest(first_name=name))
           if Riz14:
                 await Riz14(functions.account.UpdateProfileRequest(first_name=name))
           if Riz15:
                 await Riz15(functions.account.UpdateProfileRequest(first_name=name))
           if Riz16:
                 await Riz16(functions.account.UpdateProfileRequest(first_name=name))
           if Riz17:
                 await Riz17(functions.account.UpdateProfileRequest(first_name=name))
           if Riz18:
                 await Riz18(functions.account.UpdateProfileRequest(first_name=name))
           if Riz19:
                 await Riz19(functions.account.UpdateProfileRequest(first_name=name))
           if Riz20:
                 await Riz20(functions.account.UpdateProfileRequest(first_name=name))
           if Riz21:
                 await Riz21(functions.account.UpdateProfileRequest(first_name=name))
           if Riz22:
                 await Riz22(functions.account.UpdateProfileRequest(first_name=name))
           if Riz23:
                 await Riz23(functions.account.UpdateProfileRequest(first_name=name))
           if Riz24:
                 await Riz24(functions.account.UpdateProfileRequest(first_name=name))
           if Riz25:
                 await Riz25(functions.account.UpdateProfileRequest(first_name=name))
           if Riz26:
                 await Riz26(functions.account.UpdateProfileRequest(first_name=name))
           if Riz27:
                 await Riz27(functions.account.UpdateProfileRequest(first_name=name))
           if Riz28:
                 await Riz28(functions.account.UpdateProfileRequest(first_name=name))
           if Riz29:
                 await Riz29(functions.account.UpdateProfileRequest(first_name=name))
           if Riz30:
                 await Riz30(functions.account.UpdateProfileRequest(first_name=name))
           if Riz31:
                 await Riz31(functions.account.UpdateProfileRequest(first_name=name))
           if Riz32:
                 await Riz32(functions.account.UpdateProfileRequest(first_name=name))
           if Riz33:
                 await Riz33(functions.account.UpdateProfileRequest(first_name=name))
           if Riz34:
                 await Riz34(functions.account.UpdateProfileRequest(first_name=name))
           if Riz35:
                 await Riz35(functions.account.UpdateProfileRequest(first_name=name))
           if Riz36: 
                 await Riz36(functions.account.UpdateProfileRequest(first_name=name))
           if Riz37: 
                 await Riz37(functions.account.UpdateProfileRequest(first_name=name))
           if Riz38: 
                 await Riz38(functions.account.UpdateProfileRequest(first_name=name))
           if Riz39: 
                 await Riz39(functions.account.UpdateProfileRequest(first_name=name))
           if Riz40: 
                 await Riz40(functions.account.UpdateProfileRequest(first_name=name))
        except Exception as ex:
                print(ex)


@RiZoeL.on(events.NewMessage(pattern="[!/]setbio"))
async def set_bio(event):
  if event.sender_id in DEV:
     if event.is_group:
          return await event.reply("**Use this Cmd in PM !!**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message("**Send New Bio to Change The Bio**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        bio = res.message.message
        ids = 0
        hehe = await rizx.send_message("__Changing Bio..__")
        await asyncio.sleep(2)
        await hehe.edit(f"**Bio Changed Successfully ✅** \n\n **New Bio:** {bio}")
        try:
           if Riz: 
                 await Riz(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz2: 
                 await Riz2(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz3: 
                 await Riz3(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz4: 
                 await Riz4(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz5: 
                 await Riz5(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz6: 
                 await Riz6(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz7: 
                 await Riz7(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz8: 
                 await Riz8(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz9: 
                 await Riz9(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz10: 
                 await Riz10(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz11: 
                 await Riz11(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz12: 
                 await Riz12(functions.account.UpdateProfileRequest(about=bio)) 
           if Riz13: 
                 await Riz13(functions.account.UpdateProfileRequest(about=bio))
           if Riz14: 
                 await Riz14(functions.account.UpdateProfileRequest(about=bio))
           if Riz15: 
                 await Riz15(functions.account.UpdateProfileRequest(about=bio))
           if Riz16: 
                 await Riz16(functions.account.UpdateProfileRequest(about=bio))
           if Riz17: 
                 await Riz17(functions.account.UpdateProfileRequest(about=bio))
           if Riz18: 
                 await Riz18(functions.account.UpdateProfileRequest(about=bio))
           if Riz19: 
                 await Riz19(functions.account.UpdateProfileRequest(about=bio))
           if Riz20: 
                 await Riz20(functions.account.UpdateProfileRequest(about=bio))
           if Riz21: 
                 await Riz21(functions.account.UpdateProfileRequest(about=bio))
           if Riz22: 
                 await Riz22(functions.account.UpdateProfileRequest(about=bio))
           if Riz23: 
                 await Riz23(functions.account.UpdateProfileRequest(about=bio))
           if Riz24: 
                 await Riz24(functions.account.UpdateProfileRequest(about=bio))
           if Riz25: 
                 await Riz25(functions.account.UpdateProfileRequest(about=bio))
           if Riz26: 
                 await Riz26(functions.account.UpdateProfileRequest(about=bio))
           if Riz27: 
                 await Riz27(functions.account.UpdateProfileRequest(about=bio))
           if Riz28: 
                 await Riz28(functions.account.UpdateProfileRequest(about=bio))
           if Riz29: 
                 await Riz29(functions.account.UpdateProfileRequest(about=bio))
           if Riz30: 
                 await Riz30(functions.account.UpdateProfileRequest(about=bio))
           if Riz31: 
                 await Riz31(functions.account.UpdateProfileRequest(about=bio))
           if Riz32: 
                 await Riz32(functions.account.UpdateProfileRequest(about=bio))
           if Riz33: 
                 await Riz33(functions.account.UpdateProfileRequest(about=bio))
           if Riz34: 
                 await Riz34(functions.account.UpdateProfileRequest(about=bio))
           if Riz35: 
                 await Riz35(functions.account.UpdateProfileRequest(about=bio))
           if Riz36: 
                 await Riz36(functions.account.UpdateProfileRequest(about=bio))
           if Riz37: 
                 await Riz37(functions.account.UpdateProfileRequest(about=bio))
           if Riz38: 
                 await Riz38(functions.account.UpdateProfileRequest(about=bio))
           if Riz39: 
                 await Riz39(functions.account.UpdateProfileRequest(about=bio))
           if Riz40: 
                 await Riz40(functions.account.UpdateProfileRequest(about=bio))
        except Exception as ex:
                print(ex)
                        
     
