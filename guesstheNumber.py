import random
from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token,my_cell, my_twilio
client = TwilioRestClient(account_sid,auth_token)

#Wait for new SMS to arrive from SMS API
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

#Guess my number game (Nerd game :P)
def guesstheNumber(client):
    guessNum=random.randint(1,100)
    flag=True
    while flag:
        n=wait(client)
        if int(n)<1 or int(n)>100:
            client.messages.create(to=my_cell, from_=my_twilio, body="That's way off.. Try again between 1 to 100.")
        elif int(n)>guessNum:
            client.messages.create(to=my_cell,from_=my_twilio, body="Try a bit lower.")
        elif int(n)<guessNum:
            client.messages.create(to=my_cell, from_=my_twilio, body="Try a bit higher.")
        elif int(n)==guessNum:
            flag=False
            client.messages.create(to=my_cell, from_=my_twilio, body="Congrats you got it!!")


