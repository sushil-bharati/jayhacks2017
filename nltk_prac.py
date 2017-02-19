'''
Event: Jayhacks , Feb 17-19, 2017
Location: LEEP 2 Building, University of Kansas, Lawrence, 66045
Developers: Sushil, Manjish

Purpose: Virtual PC Assistant - Kiddo is developed to help any individual do the common chores as well as entertain in
much easier and modern way. Your personal PC assistant comes in two mode - Speech and Text. You can interact in either
way - through your melodious voice or through your mobile when you run sore throat.
Imagine waking up one lazy Saturday morning. How do you want to start your day? Perhaps sleep again?
Well, our specially designed assistant can play you a right music from your music library(depending on your mood) on one
go. Kiddo can update you with temperature outside so that you have the right clothes for your brisk walk. What more?
Your personalized PC assistant can update you with current twitter hashtag trends or simply keep you in conversation
if you are feeling too low. Clocks not working? Well, Kiddo has got you covered. Just ask for time and your assistant
will update you right away. Busy person? Kiddo can synchronize with your Google Calendar and help you plan out your
entire year.. or perhaps week if you are a student like me. Can you ask for more? Totally yea! Kiddo comes with built in
games (text mode) to keep you going when your best friend went for a week vacation. Did I mention that Kiddo can
read out your horoscope to you?

Future Work:
1. Integrating Artificial Intelligence to learn more sentiments of the people around
2. Implementation of Computer Vision (For example, Facial Recognition) for smart assistant
3. Further improvement on Natural Language Processing and Voice recognition software than existing
4. Making Kiddo more flexible on user end
5. Further updates(ver. Youngo)- News Headlines Reader, Movie Recommendations (personalized Machine Learning in Netflix)
'''

#import all the necessary libraries
import speech_recognition as sr
from nltk.tokenize import word_tokenize
import pyttsx
import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup

import googleCal as gcal #self-created
import dateparser as gdate #self-created
from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token,my_cell, my_twilio
import horoscope as hp #self-created
import twitter #self-created
import maingame as ent #self-created

#run speech engine - No it's not Morgan Freeman's Voice
engine = pyttsx.init()
flag = True

#kiddo vocab
terminate=["bye","goodbye","tata","adios","sayonara"]
temperature=['weather','temperature','temp','climate']
datime = ['date','time']
song = ['music','song','clip']
greetings = ['hi','hello']
schedule1 = ['schedule']
schedule2 = ['add','remind','reminder']
mode1 = ['text']
mode2 = ['voice','speech']
horo = ['horoscope']
tweet = ['twitter','trending','trend']
fun = ['game','textgame']

#Ready your audio inputs
r = sr.Recognizer()
m = sr.Microphone()

#default Attribute set up for Kiddo
myAttrib = 'speak' #default mode of personal assistant is Speech

# for listening to microphone / sms API
def listen(attr):
    if attr == 'speak':
                while True:
                    print ('Say Something...')
                    with m as source: audio = r.listen(source)
                    print("Kiddo got that! Let me check for you")
                    try:
                        #recognize_google is the google voice recognition system hosted online by google
                        spoken = r.recognize_google(audio).lower()
                        print(spoken)
                    except sr.UnknownValueError:
                        engine.say('Couldn\'t recognize that one! My Bad. Would you please repeat for me?')
                        engine.runAndWait()
                    except sr.RequestError as e:
                         print("Sphinx error; {0}".format(e))
    elif attr == 'text':
            for message in client.messages.list():
                lst = message.body
                break
            flag1 = True
            while flag1:
                for message in client.messages.list():
                    lst2 = message.body
                    break
                if lst2!=lst:
                    spoken = lst2.lower().split()
                    flag1 = False
    return spoken

#main program
try:
    while flag:
        spoken = []
        if myAttrib == 'speak':
            print ('Voice mode set')
            print("A moment of silence, please...")
            with m as source: r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Kiddo got that! Let me check for you")
            try:
                #recognize_google is the google voice recognition API by google - try sphinx for offline mode
                spoken = word_tokenize(r.recognize_google(audio).lower())
                print(spoken)
            except sr.UnknownValueError:
                engine.say('Couldn\'t recognize that one! My Bad. Would you please repeat for me?')
                engine.runAndWait()
            except sr.RequestError as e:
                 print("Sphinx error; {0}".format(e))
        elif myAttrib == 'text':
            client = TwilioRestClient(account_sid,auth_token) #connect with twilio SMS API
            print ('Text mode set')
            for message in client.messages.list():
                lst = message.body
                break
            flag1 = True
            while flag1:
                for message in client.messages.list():
                    lst2 = message.body
                    break
                if lst2!=lst:
                    spoken = lst2.lower().split()
                    flag1 = False



        if any(words in spoken for words in temperature): #temperature update
            response = urlopen('https://www.wunderground.com/us/ks/lawrence').read()
            soup = BeautifulSoup(response,'html.parser')
            tags1 = soup.find_all("div",id='curFeel')
            tags2 = soup.find_all("div",id='curTemp')
            for tag in tags1:
                s1 = tag.find("span", class_='wx-value').get_text()
            for tag in tags2:
                s2 = tag.find("span", class_='wx-value').get_text()
            response = urlopen('http://forecast.weather.gov/MapClick.php?CityName=Lawrence&state=KS&site=TOP&lat=38.9629&lon=-95.2554').read()
            finalstr=""
            soup = BeautifulSoup(response,'html.parser')
            tags1 = soup.find_all("div",class_="row row-odd row-forecast")
            finalstr = tags1[0].find("div",class_="col-sm-10 forecast-text").get_text()
            tempFeel = round(5/9 * (float(s1) - 32),1)
            tempCur = round(5/9 * (float(s2) - 32),1)
            str = "Outside temperature is {}, but feels like {} degree celsius to me. Additionally, it is gonna be {}".format(tempCur, tempFeel, finalstr)
            if myAttrib == 'speak': engine.say(str)
            if myAttrib == 'text': client.messages.create(to=my_cell,from_=my_twilio, body=str)
        elif any(words in spoken for words in terminate): #terminate Kiddo - like THE Terminator :P
            flag = False
            msg = 'GoodBye!! Have a nice day.'
            if myAttrib == 'speak': engine.say(msg)
            if myAttrib == 'text': client.messages.create(to=my_cell,from_=my_twilio, body=msg)
        elif any(words in spoken for words in greetings): #greeting
             msg = 'Hi. I am Kiddo. How can I help you today?'
             if myAttrib == 'speak': engine.say(msg)
             if myAttrib == 'text': client.messages.create(to=my_cell,from_=my_twilio, body=msg)
        elif 'name' in spoken: #kiddo build in info
            msg = 'I am glad you asked that. My name is Kiddo. I am built by Sushil and Manjish on Feb 17, 2017 night for Jayhack!'
            if myAttrib == 'speak': engine.say(msg)
            if myAttrib == 'text': client.messages.create(to=my_cell,from_=my_twilio, body=msg)
        elif any(words2 in spoken for words2 in song): #play song
            from pygame import mixer
            msg = 'Sure. Which artist would you like to listen to from your library?.'
            if myAttrib == 'speak':
                engine.say(msg)
                engine.runAndWait()
            if myAttrib == 'text': client.messages.create(to=my_cell,from_=my_twilio, body=msg)
            ##
            val = listen(myAttrib)
            ##
            strMusic = 'F:\\workout_music\\'+''.join(val)+'.mp3'
            mixer.init()
            mixer.music.load(strMusic)
            mixer.music.play()
            k = 0
            while mixer.music.get_busy():
                k += 1
            flag = False
        elif any(words2 in spoken for words2 in datime): #date - time update
            import datetime
            date = datetime.datetime.now().strftime('%A-%B-%d-%H-%M-%S').split('-')
            str = "My calendar shows {} {} and the time is {} hours {} minutes.".format(date[1],date[2],date[3],date[4])
            if myAttrib == 'speak':
                engine.say(str)
                engine.runAndWait()
            elif myAttrib == 'text':
                client.messages.create(to=my_cell,from_=my_twilio, body=str)
        elif 'love' in spoken: #we thought of putting this one for all the singles out there ;)
            str = 'I love you too.'
            if myAttrib == 'speak':
                engine.say(str)
                engine.runAndWait()
            elif myAttrib == 'text':
                client.messages.create(to=my_cell,from_=my_twilio, body=str)
        elif any(words in spoken for words in schedule1) and myAttrib=='speak': #Google calendar API integration
            events = gcal.getTodayEvent()
            cnt = 1
            for evt in (events['items']):
                    hr = evt['start']['dateTime'][11:13]
                    min = evt['start']['dateTime'][14:16]
                    print (hr,min)
                    #engine.say(evt['end']['dateTime'])
                    if str(min) != '00':
                        strAdd = str(min) + 'mins'
                    else:
                        strAdd=''
                    if cnt == 1:
                        firstStr = 'Today'
                        cnt += 1
                    else:
                        firstStr = 'and'
                    strSpeak = firstStr + ' you have ' + evt['summary'] + ' at ' + str(hr) + ' hours ' + strAdd
                    if myAttrib == 'speak':
                        engine.say(strSpeak)
                        engine.runAndWait()
                    elif myAttrib == 'text':
                        client.messages.create(to=my_cell,from_=my_twilio, body=strSpeak)
            if (events['items']==[]): # No events today
                msg = 'I see you have a rest day today! Enjoy!'
                if myAttrib == 'speak':
                    engine.say(msg)
                    engine.runAndWait()
                elif myAttrib == 'text':
                    client.messages.create(to=my_cell,from_=my_twilio, body=msg)
        elif any(words in spoken for words in schedule2): #Ask Event title
            CAL = gcal.connectGoogleCal()
            msg = 'Okay. I have your Google calendar ready. What should be the title of your event?'
            engine.say(msg)
            engine.runAndWait()
            while True:
                print ('Say Something...')
                with m as source: audio = r.listen(source)
                print("Kiddo got that! Let me check for you")
                try:
                    title1 = r.recognize_google(audio).lower()
                    if spoken != '': break
                    print(spoken)
                except sr.UnknownValueError:
                    engine.say('Couldn\'t recognize that one! My Bad. Would you please repeat for me?')
                except sr.RequestError as e:
                     print("Sphinx error; {0}".format(e))
            print(title1)
            engine.say('When is this event?') #Ask Event date
            engine.runAndWait()
            while True:
                print ('Say Something...')
                with m as source: audio = r.listen(source)
                print("Kiddo got that! Let me check for you")
                try:
                    #recognize_google is the google voice recognition system hosted online by google
                    title2 = r.recognize_google(audio).lower()
                    if spoken != '': break
                    print(spoken)
                except sr.UnknownValueError:
                    engine.say('Couldn\'t recognize that one! My Bad. Would you please repeat for me?')
                except sr.RequestError as e:
                     print("Sphinx error; {0}".format(e))
            print(title2)
            realTime = gdate.grabTime(title2)
            print(realTime)
            ###
            engine.say('When does your' + title1 + ' end?')
            engine.runAndWait()
            while True:
                print ('Say Something...')
                with m as source: audio = r.listen(source)
                print("Kiddo got that! Let me check for you")
                try:
                    title3 = r.recognize_google(audio).lower()
                    if spoken != '': break
                    print(spoken)
                except sr.UnknownValueError:
                    engine.say('Couldn\'t recognize that one! My Bad. Would you please repeat for me?')
                except sr.RequestError as e:
                     print("Sphinx error; {0}".format(e))
            print(title3)
            realTime2 = gdate.grabTime(title3)
            print(realTime2)
            ##
            gcal.createCalEvent(realTime,realTime2,title1)
        elif any(words in spoken for words in horo): #Horoscope feature
            strSpeak = 'What is your sun sign?'
            if myAttrib == 'speak':
                    engine.say(strSpeak)
                    engine.runAndWait()
            elif myAttrib == 'text':
                    client.messages.create(to=my_cell,from_=my_twilio, body=strSpeak)
            sign = ''.join(listen(myAttrib))
            h = hp.horoscopedaily(sign)
            if myAttrib == 'speak':
                    engine.say(h)
                    engine.runAndWait()
            elif myAttrib == 'text':
                    client.messages.create(to=my_cell,from_=my_twilio, body=h)
        elif any(words in spoken for words in tweet): #Twitter trends
            trendList = twitter.getTrending()
            if myAttrib == 'speak':
                engine.say('The most trending tweets right now in twitter are ')
                for i in range(0,5):
                    engine.say(trendList[i]+'')
                    engine.runAndWait()
            elif myAttrib == 'text':
                strng=''
                for i in range(0,5):
                    j = i + 1
                    strng += str(j) + '. ' +trendList[i] + '\n'
                client.messages.create(to=my_cell,from_=my_twilio, body=strng)
        elif any(words in spoken for words in fun):
            ent.playGame(client)
        elif any(words3 in spoken for words3 in mode1):
            myAttrib = 'text'
        elif any(words3 in spoken for words3 in mode2):
            myAttrib = 'speak'

        engine.runAndWait()


except KeyboardInterrupt:
    pass




