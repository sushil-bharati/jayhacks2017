from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token,my_cell, my_twilio
import rockpaperscissor as game1
import guesstheNumber as game2

# wait for new SMS to arrive from SMS API
def wait(client):
    for message in client.messages.list():
        lst = message.body
        break
    while True:
        for message in client.messages.list():
            lst2 = message.body
            break
        if lst2 != lst:
            lst = lst2
            lst2 = ''
            return lst

#game play algo
def playGame(client):
    my_msg="Game \n1. Rock Paper Scissor \n2.Guess my number"
    message=client.messages.create(to=my_cell,from_=my_twilio, body=my_msg)
    val=wait(client)
    if val=='1':
        client.messages.create(to=my_cell, from_=my_twilio, body='Enter: Rock Paper or Scissor')
        flag = True
        while flag:
            val=wait(client)
            result=game1.rockPaperScissor(val)
            client.messages.create(to=my_cell,from_=my_twilio, body=result)
            if result != "Wrong entry, Type correctly":
                flag = False
    elif val=='2':
        client.messages.create(to=my_cell, from_=my_twilio, body='Enter number between 1 to 100')
        game2.guesstheNumber(client)
    else:
        client.messages.create(to=my_cell, from_=my_twilio, body="I can't find game with that index..")

