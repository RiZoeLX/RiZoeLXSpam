import os 
import asyncio
from telethon import events
from datetime import datetime
from RiZoeLXSpam import STRING, STRING2, STRING3, STRING4, STRING5 , STRING6, STRING7, STRING8, STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29, STRING30, STRING31, STRING32, STRING33, STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40
from telethon.tl.types import InputPeerChannel
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError, FloodWaitError, RPCError

ABORT = "**All process Cancelled !**"

@RiZoeL.on(events.NewMessage(pattern="[!/]scrape"))
async def scrape(event):
  if event.sender_id in DEV:
     if event.is_group:
          return await event.reply("**Use this Cmd in PM !!**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        fuk = event.chat_id
        await rizx.send_message("**Send Group Link Were You Want To add Members !**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        grpp = res.message.message
        if grpp.startswith("https://t.me/") or grpp.startswith("@"):
              add_grp = grpp
              k = await Riz.get_entity(add_grp)
              grp_id = k.id
        else:
            await rizx.send_message("Error! Send Group link or Username")
            return
        await rizx.send_message("**Send Group link or username For scraping**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        grpp2 = res.message.message
        if grpp.startswith("https://t.me/") or grpp.startswith("@"):
              scrape_grp = grpp2
              k = await Riz.get_entity(scrape_grp)
              grp_id2 = k.id
        else:
            await rizx.send_message("Error! Send Group link or Username")
            return
        await rizx.send_message("**Send String No. of IDs From Which You Want To add members**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        Num = res.message.message
        if Num.isnumeric():
             id = int(Num)
        else:
            await rizx.send_message("Error! Send Count in Numbers")
            return
        if Num == "1":
           try:
              await Riz(JoinChannelRequest(scrape_grp))
              await Riz(JoinChannelRequest(add_grp))
              peer = 0
              a = 0
              await rizx.send_message(f"**Adding Users In : {add_grp}**")
              Add_Msg = await Riz.send_message(grp_id, f"__️Scraping Users From {scrape_grp}__")
              async for sex in Riz.iter_participants(scrape_grp, aggressive=True):
                 print(f"Adding Started In {add_grp} By ID: {id}")
                 try:
                    await Riz(InviteToChannelRequest(add_grp, [sex]))
                    await asyncio.sleep(3)
                    a += 1
                 except FloodWaitError as s:
                    print(f"FloodwaitError For {s.seconds}")
                    await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                    return
                 except UserPrivacyRestrictedError:
                    print("PrivacyRestrictedError")
                 except UserAlreadyParticipantError:
                    print("User Already In Group")
                 except UserBannedInChannelError:
                    print("User Banned in Group")
                 except ChatAdminRequiredError:
                    print("Error: To Add Members Chat Admin Required")
                    await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                    return
                 except ValueError:
                    print(f"Error: Can't Find Group/channel")
                    await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                    return
                 except PeerFloodError:
                  if peer == 10:
                    print("PeerFloodError")
                    peer += 1  
                    await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                    return
                 except ChatWriteForbiddenError as fuk:
                    await Riz(JoinChannelRequest(add_grp))
                    continue
                 except RPCError as ok:
                    print(f"ok.__class__.__name__")
                 except Exception as e:
                    print(e)
              return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
           except Exception as sex:
               print(sex)
    
        elif Num == "2":
           if STRING2:
              try:
                 await Riz2(JoinChannelRequest(scrape_grp))
                 await Riz2(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz2.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz2.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz2(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz2(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING2` then Try Again")
    
    
        elif Num == "3":
           if STRING3:
              try:
                 await Riz3(JoinChannelRequest(scrape_grp))
                 await Riz3(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz3.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz3.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz3(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz3(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING3` then Try Again")

        elif Num == "4":
           if STRING4:
              try:
                 await Riz4(JoinChannelRequest(scrape_grp))
                 await Riz5(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz4.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz4.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz4(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz4(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING4` then Try Again")

        elif Num == "5":
           if STRING5:
              try:
                 await Riz5(JoinChannelRequest(scrape_grp))
                 await Riz5(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz5.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz5.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz5(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz5(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING5` then Try Again")

        elif Num == "6":
           if STRING6:
              try:
                 await Riz6(JoinChannelRequest(scrape_grp))
                 await Riz6(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz6.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz6.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz6(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       await rizx.send_message(f"**Reply Raid Activated on {fukname} 🔥**")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz6(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING6` then Try Again")

        elif Num == "7":
           if STRING7:
              try:
                 await Riz7(JoinChannelRequest(scrape_grp))
                 await Riz7(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz7.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz7.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz7(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz7(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING7` then Try Again")

        elif Num == "8":
           if STRING8:
              try:
                 await Riz8(JoinChannelRequest(scrape_grp))
                 await Riz8(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz8.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz8.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz8(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz8(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING8` then Try Again")

        elif Num == "9":
           if STRING9:
              try:
                 await Riz9(JoinChannelRequest(scrape_grp))
                 await Riz9(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz9.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz9.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz9(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz9(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING9` then Try Again")

        elif Num == "10":
           if STRING10:
              try:
                 await Riz10(JoinChannelRequest(scrape_grp))
                 await Riz10(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz10(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz10(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING10` then Try Again")

        elif Num == "11":
           if STRING11:
              try:
                 await Riz11(JoinChannelRequest(scrape_grp))
                 await Riz11(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz11.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz11.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz11(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz11(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING11` then Try Again")

        elif Num == "12":
           if STRING12:
              try:
                 await Riz12(JoinChannelRequest(scrape_grp))
                 await Riz12(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz12.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz12.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz12(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz12(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING12` then Try Again")

        elif Num == "13":
           if STRING13:
              try:
                 await Riz13(JoinChannelRequest(scrape_grp))
                 await Riz13(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz13.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz13.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz13(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz13(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING13` then Try Again")

        elif Num == "14":
           if STRING14:
              try:
                 await Riz14(JoinChannelRequest(scrape_grp))
                 await Riz14(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz14.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz14.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz14(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz14(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING14` then Try Again")

        elif Num == "15":
           if STRING15:
              try:
                 await Riz15(JoinChannelRequest(scrape_grp))
                 await Riz15(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz15.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz15.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz15(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz15(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING15` then Try Again")

        elif Num == "16":
           if STRING16:
              try:
                 await Riz16(JoinChannelRequest(scrape_grp))
                 await Riz16(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz16.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz16.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz16(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz16(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING16` then Try Again")

        elif Num == "17":
           if STRING17:
              try:
                 await Riz17(JoinChannelRequest(scrape_grp))
                 await Riz17(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz17.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz17.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz17(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz17(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING17` then Try Again")

        elif Num == "18":
           if STRING18:
              try:
                 await Riz18(JoinChannelRequest(scrape_grp))
                 await Riz18(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz18.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz18.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz18(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz18(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING18` then Try Again")

        elif Num == "19":
           if STRING19:
              try:
                 await Riz19(JoinChannelRequest(scrape_grp))
                 await Riz19(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz19.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz19.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz19(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz19(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING19` then Try Again")

        elif Num == "20":
           if STRING20:
              try:
                 await Riz20(JoinChannelRequest(scrape_grp))
                 await Riz20(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz20.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz20.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz20(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz20(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING20` then Try Again")

        elif Num == "21":
           if STRING21:
              try:
                 await Riz21(JoinChannelRequest(scrape_grp))
                 await Riz21(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz21.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz21.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz21(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz21(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING21` then Try Again")

        elif Num == "22":
           if STRING22:
              try:
                 await Riz22(JoinChannelRequest(scrape_grp))
                 await Riz22(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz22.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz22.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz22(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz22(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING22` then Try Again")

        elif Num == "23":
           if STRING23:
              try:
                 await Riz23(JoinChannelRequest(scrape_grp))
                 await Riz23(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz23.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz23.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz23(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz23(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING23` then Try Again")

        elif Num == "24":
           if STRING24:
              try:
                 await Riz24(JoinChannelRequest(scrape_grp))
                 await Riz24(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz24.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz24.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz24(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz24(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING24` then Try Again")

        elif Num == "25":
           if STRING25:
              try:
                 await Riz25(JoinChannelRequest(scrape_grp))
                 await Riz25(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz25.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz25.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz25(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz25(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING25` then Try Again")

        elif Num == "26":
           if STRING26:
              try:
                 await Riz26(JoinChannelRequest(scrape_grp))
                 await Riz26(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz26.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz26.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz26(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz26(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING26` then Try Again")

        elif Num == "27":
           if STRING27:
              try:
                 await Riz27(JoinChannelRequest(scrape_grp))
                 await Riz27(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz27.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz27.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz27(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz27(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING27` then Try Again")

        elif Num == "28":
           if STRING28:
              try:
                 await Riz28(JoinChannelRequest(scrape_grp))
                 await Riz28(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz28.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz28.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz28(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz28(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING28` then Try Again")

        elif Num == "29":
           if STRING29:
              try:
                 await Riz29(JoinChannelRequest(scrape_grp))
                 await Riz29(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz29.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz29.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz29(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz29(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING29` then Try Again")

        elif Num == "30":
           if STRING30:
              try:
                 await Riz30(JoinChannelRequest(scrape_grp))
                 await Riz30(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz30.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz30.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz30(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz30(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING30` then Try Again")

        elif Num == "31":
           if STRING31:
              try:
                 await Riz31(JoinChannelRequest(scrape_grp))
                 await Riz31(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz31.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz31.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz31(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz31(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING31` then Try Again")

        elif Num == "32":
           if STRING32:
              try:
                 await Riz32(JoinChannelRequest(scrape_grp))
                 await Riz32(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz32.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz32.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz32(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz32(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING32` then Try Again")

        elif Num == "33":
           if STRING33:
              try:
                 await Riz33(JoinChannelRequest(scrape_grp))
                 await Riz33(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz33.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz33.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz33(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz33(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING33` then Try Again")

        elif Num == "34":
           if STRING34:
              try:
                 await Riz34(JoinChannelRequest(scrape_grp))
                 await Riz34(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz34.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz34.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz34(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz34(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING34` then Try Again")

        elif Num == "35":
           if STRING35:
              try:
                 await Riz35(JoinChannelRequest(scrape_grp))
                 await Riz35(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz35.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz35.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz35(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz35(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING35` then Try Again")

        elif Num == "36":
           if STRING36:
              try:
                 await Riz36(JoinChannelRequest(scrape_grp))
                 await Riz36(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz36.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz36.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz36(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz36(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING36` then Try Again")

        elif Num == "37":
           if STRING37:
              try:
                 await Riz37(JoinChannelRequest(scrape_grp))
                 await Riz37(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz37.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz37.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz37(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz37(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING37` then Try Again")

        elif Num == "38":
           if STRING38:
              try:
                 await Riz38(JoinChannelRequest(scrape_grp))
                 await Riz38(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz38.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz38.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz38(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz38(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING38` then Try Again")

        elif Num == "39":
           if STRING39:
              try:
                 await Riz39(JoinChannelRequest(scrape_grp))
                 await Riz39(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz39.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz39.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz39(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz39(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING39` then Try Again")

        elif Num == "40":
           if STRING40:
              try:
                 await Riz40(JoinChannelRequest(scrape_grp))
                 await Riz40(JoinChannelRequest(add_grp))
                 peer = 0
                 a = 0
                 await rizx.send_message(f"**Adding Users In : {add_grp}**")
                 Add_Msg = await Riz40.send_message(grp_id, f"__Scraping Users From {scrape_grp}__")
                 async for sex in Riz40.iter_participants(scrape_grp, aggressive=True):
                    print(f"Adding Started In {add_grp} By ID: {id}")
                    try:
                       await Riz40(InviteToChannelRequest(add_grp, [sex]))
                       await asyncio.sleep(3)
                       a += 1
                    except FloodWaitError as s:
                       print(f"FloodwaitError For {s.seconds}")
                       await rizx.send_message(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Try With New ID**")
                       return
                    except UserPrivacyRestrictedError:
                       print("PrivacyRestrictedError")
                    except UserAlreadyParticipantError:
                       print("User Already In Group")
                    except UserBannedInChannelError:
                       print("User Banned in Group")
                    except ChatAdminRequiredError:
                       print("Error: To Add Members Chat Admin Required")
                       await rizx.send_message(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                       return
                    except ValueError:
                       print(f"Error: Can't Find Group/channel")
                       await rizx.send_message(f"**Error 204 !!** \n Can't Find Group/Channel")
                       return
                    except PeerFloodError:
                      if peer == 10:
                        print("PeerFloodError")
                        peer += 1  
                        await rizx.send_message(f"**Error 102 !!** \n PeerFloodError !")
                        return
                    except ChatWriteForbiddenError as fuk:
                       await Riz40(JoinChannelRequest(add_grp))
                       continue
                    except RPCError as ok:
                       print(f"ok.__class__.__name__")
                    except Exception as e:
                       print(e)
                 return await Add_Msg.edit(f"**Scraping Users** \n\n • __From Chat:__ {scrape_grp} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
              except Exception as sex:
                  print(sex)
           else:
               await rizx.send_message(f"**ERROR 404!!** \n\n Add `STRING40` then Try Again")
        else:
            await rizx.send_message(f"**ERROR !!** \n\n __send no. Between 1 to 40__")
