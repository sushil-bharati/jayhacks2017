import tweepy

#Use your own keys - just for demo purpose
consumerKey = 'mO8Z9zMAMXJNSVik2Yz5U39LE'
consumerSecret = 'QtgjP7pPP6sou61GL2hk4fmiT1BkDe952pVQ9pnwrwMZXTbHei'
accessToken = '124438153-UbL8anIPov6TiMa90xK9HSahU6MsnQrXQoy9fCEF'
accessTokenSecret = 'OXsGVW749u85Y8Eogh75W7V19xhax0cLoDY8Dt2CqisAS'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#get twitter hastags
def getTrending():
    trends1 = api.trends_place(1)
    hashtags = [x['name'] for x in trends1[0]['trends'] if x['name'].startswith('#')]
    return hashtags

