from rivescript import RiveScript

cs = RiveScript()

cs.load_directory("brain")
cs.sort_replies()

def chat(message):
    if message == "":
        return "no message found"
    else:
        response = cs.reply( "user",message)
    if response:
        return  response
    else:
        return "no response found"
          
    
#to test bot in terminal 
# while True:
#     msg=str(input ("user: "))
#     reply = str(cs.reply('localuser',msg))
#     if msg == "quit":
#         break
#     else:
#         print('Bot: '+ reply)