from core.utility.strings import str_service

def init(update):
    first_name = str(update.effective_user.first_name)
    userid = str(update.effective_user.id)
    text = str(update.effective_message.text)
    chatname = str(update.effective_chat.title)
    chatid = str(update.effective_chat.id)
    print(str_service.DEBUG_MESSAGE.format(first_name,userid,text,chatname,chatid))