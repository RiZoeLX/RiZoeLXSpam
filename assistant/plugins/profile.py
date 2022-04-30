import asyncio
import os
from telethon.tl import functions
from telethon import events
from telethon.tl.functions.photos import UploadProfilePhotoRequest

@RiZoeL.on(events.NewMessage(pattern="[!/]setname"))
async def set_name(event):
     if event.sender_id not in DEV:
             return
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
     if event.sender_id not in DEV:
             return
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
                        
        
@RiZoeL.on(events.NewMessage(pattern="[!/]setpic"))        
async def setpfp(event):
  if event.sender_id in DEV:
     if event.is_group:
          return await event.reply("**Use this Cmd in PM !!**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        photo = None
        await rizx.send_message("**Send Pic to Change Profile pic**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        pfp = res.message.message
        try:
           photo = await pfp.download_media("resources/downloads/")
        except:
           pass
        hehe = await rizx.send_message("__Changing profile pic..__")
        await asyncio.sleep(3)
        await hehe.edit(f"**Profile Pic Successfully ✅**")
        try:
           if Riz: 
                 await Riz(UploadProfilePhotoRequest(await Riz.upload_file(photo))) 
           if Riz2: 
                 await Riz2(UploadProfilePhotoRequest(await Riz2.upload_file(photo))) 
           if Riz3: 
                 await Riz3(UploadProfilePhotoRequest(await Riz3.upload_file(photo))) 
           if Riz4: 
                 await Riz4(UploadProfilePhotoRequest(await Riz4.upload_file(photo))) 
           if Riz5: 
                 await Riz5(UploadProfilePhotoRequest(await Riz5.upload_file(photo))) 
           if Riz6: 
                 await Riz6(UploadProfilePhotoRequest(await Riz6.upload_file(photo))) 
           if Riz7: 
                 await Riz7(UploadProfilePhotoRequest(await Riz7.upload_file(photo))) 
           if Riz8: 
                 await Riz8(UploadProfilePhotoRequest(await Riz8.upload_file(photo))) 
           if Riz9: 
                 await Riz9(UploadProfilePhotoRequest(await Riz9.upload_file(photo))) 
           if Riz10: 
                 await Riz10(UploadProfilePhotoRequest(await Riz10.upload_file(photo))) 
           if Riz11: 
                 await Riz11(UploadProfilePhotoRequest(await Riz11.upload_file(photo))) 
           if Riz12: 
                 await Riz12(UploadProfilePhotoRequest(await Riz12.upload_file(photo))) 
           if Riz13: 
                 await Riz13(UploadProfilePhotoRequest(await Riz13.upload_file(photo)))
           if Riz14: 
                 await Riz14(UploadProfilePhotoRequest(await Riz14.upload_file(photo)))
           if Riz15: 
                 await Riz15(UploadProfilePhotoRequest(await Riz15.upload_file(photo)))
           if Riz16: 
                 await Riz16(UploadProfilePhotoRequest(await Riz16.upload_file(photo)))
           if Riz17: 
                 await Riz17(UploadProfilePhotoRequest(await Riz17.upload_file(photo)))
           if Riz18: 
                 await Riz18(UploadProfilePhotoRequest(await Riz18.upload_file(photo)))
           if Riz19: 
                 await Riz19(UploadProfilePhotoRequest(await Riz19.upload_file(photo)))
           if Riz20: 
                 await Riz20(UploadProfilePhotoRequest(await Riz20.upload_file(photo)))
           if Riz21: 
                 await Riz21(UploadProfilePhotoRequest(await Riz21.upload_file(photo)))
           if Riz22: 
                 await Riz22(UploadProfilePhotoRequest(await Riz22.upload_file(photo)))
           if Riz23: 
                 await Riz23(UploadProfilePhotoRequest(await Riz23.upload_file(photo)))
           if Riz24: 
                 await Riz24(UploadProfilePhotoRequest(await Riz24.upload_file(photo)))
           if Riz25: 
                 await Riz25(UploadProfilePhotoRequest(await Riz25.upload_file(photo)))
           if Riz26: 
                 await Riz26(UploadProfilePhotoRequest(await Riz26.upload_file(photo)))
           if Riz27: 
                 await Riz27(UploadProfilePhotoRequest(await Riz27.upload_file(photo)))
           if Riz28: 
                 await Riz28(UploadProfilePhotoRequest(await Riz28.upload_file(photo)))
           if Riz29: 
                 await Riz29(UploadProfilePhotoRequest(await Riz29.upload_file(photo)))
           if Riz30: 
                 await Riz30(UploadProfilePhotoRequest(await Riz30.upload_file(photo)))
           if Riz31: 
                 await Riz31(UploadProfilePhotoRequest(await Riz31.upload_file(photo)))
           if Riz32: 
                 await Riz32(UploadProfilePhotoRequest(await Riz32.upload_file(photo)))
           if Riz33: 
                 await Riz33(UploadProfilePhotoRequest(await Riz33.upload_file(photo)))
           if Riz34: 
                 await Riz34(UploadProfilePhotoRequest(await Riz34.upload_file(photo)))
           if Riz35: 
                 await Riz35(UploadProfilePhotoRequest(await Riz35.upload_file(photo)))
           if Riz36: 
                 await Riz36(UploadProfilePhotoRequest(await Riz36.upload_file(photo)))
           if Riz37: 
                 await Riz37(UploadProfilePhotoRequest(await Riz37.upload_file(photo)))
           if Riz38: 
                 await Riz38(UploadProfilePhotoRequest(await Riz38.upload_file(photo)))
           if Riz39: 
                 await Riz39(UploadProfilePhotoRequest(await Riz39.upload_file(photo)))
           if Riz40: 
                 await Riz40(UploadProfilePhotoRequest(await Riz40.upload_file(photo)))
           try:
               os.remove(media)
           except Excepion as e:
               print(str(e))

        except Exception as ex:
                print(ex)
