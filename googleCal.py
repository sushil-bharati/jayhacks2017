from httplib2 import Http
from oauth2client import file, client, tools
import apiclient
import datetime

#Connect with Google Calendar API
def connectGoogleCal():
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)
    return apiclient.discovery.build('calendar', 'v3', http=creds.authorize(Http()))

#Create calendar event for given startime, endtime and title of the event
def createCalEvent(startTime,endTime,title):
    CAL = connectGoogleCal()
    GMT_OFF = '-06:00'      # PDT/MST/GMT-7
    time = startTime +':00%s' % GMT_OFF
    time2 = endTime +':00%s' % GMT_OFF
    EVENT = {
        'summary': title,
        'start':  {'dateTime': time},
        'end':    {'dateTime': time2},
        #'attendees': [
         #   {'email': 'friend1@example.com'},
         #   {'email': 'friend2@example.com'},
        #],
    }
    e = CAL.events().insert(calendarId='primary', sendNotifications=True, body=EVENT).execute() #insert event in google cal

#To grab todays event
def getTodayEvent():
    CAL = connectGoogleCal()
    strStart = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S-06:00') #string converted current datetime

    myTime = datetime.datetime.strptime(strStart, '%Y-%m-%dT%H:%M:%S-06:00')
    myTime += datetime.timedelta(hours=24) #

    strEnd = myTime.strftime('%Y-%m-%dT%H:%M:%S-06:00') #string converted datetime after 24 hours

    return CAL.events().list(calendarId='primary',timeMin=strStart, timeMax=strEnd).execute()

#
# if datetime.datetime.strptime(evt['start']['dateTime'],"%Y-%m-%dT%H:%M:%S-%W:%U")[0:10] > datetime.datetime.now():
#         print(evt['summary'])
# event = CAL.events().get(calendarId='primary', eventId='Dinner with friends').execute()
# print (event['summary'])
# print (e)
# print('''*** %r event added:
#     Start: %s
#     End:   %s''' % (e2['summary'].encode('utf-8'),
#         e2['start']['dateTime'], e2['end']['dateTime']))
# page_token = None
# while True:
#   events = CAL.events().list(calendarId='primary', pageToken=page_token).execute()
#   for event in events['items']:
#     print (event['summary'])
#   page_token = events.get('nextPageToken')
#   if not page_token:
#     break
