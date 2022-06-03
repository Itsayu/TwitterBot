import tweepy

consumer_key = 'use your consumer key'
consumer_secret = 'use your consumer secret'
access_token = 'use your access token'
access_token_secret = 'use your access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status('Hey Folks...!')
