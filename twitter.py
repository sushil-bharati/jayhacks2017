import tweepy

#Use your own keys - just for demo purpose
consumerKey = 'XX'
consumerSecret = 'XX'
accessToken = '1XX'
accessTokenSecret = 'OXX'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#get twitter hastags
def getTrending():
    trends1 = api.trends_place(1)
    hashtags = [x['name'] for x in trends1[0]['trends'] if x['name'].startswith('#')]
    return hashtags

