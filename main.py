import tweepy

consumer_key = 'KvANtIhF89JvRMxeyJFfKN2Av'
consumer_secret = 'CjXjIVevlu96LeVTyXkvlFuIweMAVBXAtFa2ymMKLpSYLqe5i3'
access_token = '1172074378353229824-Q5PNl31DHV7AC8HrChvFFtiFwztjNh'
access_token_secret = 'U2sJ9LGzbZPVV0EbBaYRtn5LI3T4bn7WFT6gvZ6eGDIXg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status('Hey Folks...!')

# tweets = api.mentions_timeline()
# print(tweets[4].text)

# -----------------PRINT ALL MENTION TWEET (WITHOUT ANY CONDITION)------------------

# for tweet in tweets:
#     print(str(tweet.id) + ' - ' + tweet.text)

# -------------WITH CONDITION-------------
# for tweet in tweets:
#     if '#aktweet' in tweet.text:
#         print("New Tweet Found!")
#         print(str(tweet.id) + ' - ' + tweet.text)


