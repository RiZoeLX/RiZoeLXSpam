@RiZoeL.on(events.NewMessage(pattern="[!/]spam"))
async def spam(event):
     if event.sender_id not in DEV or event.sender_id not in SUDO_USERS:
             return
     if event.is_group:
          return await event.reply("**Use This Cmd In PM**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message(SEND_GRP)
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        grpp = res.message.message
        if grpp.startswith("https://t.me/") or grpp.startswith("@"):
              spam_group = grpp
              if spam_group in GRP:
                  return await rizx.send_message("Sorry !! I can't Spam there")
              k = await Riz.get_entity(spam_group)
              grp_id = k.id
        else:
            await rizx.send_message("Error! Send Group link or Username")
            return
        await rizx.send_message(SEND_COUNT)
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        Num = res.message.message
        if Num.isnumeric():
             count = int(Num)
        else:
            await rizx.send_message("Error! Send Count in Numbers")
            return
        await rizx.send_message(SEND_SPAM)
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        message = res.message.message
        Fukoff = await rizx.send_message(f"__Starting Spam In {spam_group}__")
        await asyncio.sleep(2)
        await Fukoff.edit(f"**▪️Started Spam ▪️** \n\n__Group__ : `{spam_group}`\n__Spam Count__ : `{count}` \n__Spam Message__ : `{message}`")     
        ids = 0
        try:
           if Riz:
                 ids += 1
                 await Riz(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz2:
                 ids += 1
                 await Riz2(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz2.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz3:
                 ids += 1
                 await Riz3(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz3.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz4:
                 ids += 1
                 await Riz4(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz4.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz5:
                 ids += 1
                 await Riz5(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz5.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz6:
                 ids += 1
                 await Riz6(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz6.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz7:
                 ids += 1
                 await Riz7(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz7.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz8:
                 ids += 1
                 await Riz8(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz8.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz9:
                 ids += 1
                 await Riz9(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz9.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz10:
                 ids += 1
                 await Riz10(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz10.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz11:
                 ids += 1
                 await Riz11(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz11.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz12:
                 ids += 1
                 await Riz12(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz12.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz13:
                 ids += 1
                 await Riz13(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz13.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz14:
                 ids += 1
                 await Riz14(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz14.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz15:
                 ids += 1
                 await Riz15(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz15.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz16:
                 ids += 1
                 await Riz16(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz16.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz17:
                 ids += 1
                 await Riz17(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz17.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz18:
                 ids += 1
                 await Riz18(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz18.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz19:
                 ids += 1
                 await Riz19(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz19.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz20:
                 ids += 1
                 await Riz20(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz20.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz21:
                 ids += 1
                 await Riz21(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz21.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz22:
                 ids += 1
                 await Riz22(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz22.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz23:
                 ids += 1
                 await Riz23(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz23.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz24:
                 ids += 1
                 await Riz24(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz24.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz25:
                 ids += 1
                 await Riz25(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz25.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz26:
                 ids += 1
                 await Riz26(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz26.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz27:
                 ids += 1
                 await Riz27(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz27.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz28:
                 ids += 1
                 await Riz28(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz28.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz29:
                 ids += 1
                 await Riz29(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz29.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz30:
                 ids += 1
                 await Riz30(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz30.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz31:
                 ids += 1
                 await Riz31(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz31.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz32:
                 ids += 1
                 await Riz32(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz32.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz33:
                 ids += 1
                 await Riz33(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz33.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz34:
                 ids += 1
                 await Riz34(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz34.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz35:
                 ids += 1
                 await Riz35(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz35.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz36:
                 ids += 1
                 await Riz36(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz36.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz37:
                 ids += 1
                 await Riz37(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz37.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz38:
                 ids += 1
                 await Riz38(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz38.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz39:
                 ids += 1
                 await Riz39(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz39.send_message(grp_id, message)
                        await asyncio.sleep(0.3)
           if Riz40:
                 ids += 1
                 await Riz40(functions.channels.JoinChannelRequest(channel=spam_group))
                 for _ in range(count):
                        await Riz40.send_message(grp_id, message)
                        await asyncio.sleep(0.3) 
        except Exception as ex:
                print(ex)