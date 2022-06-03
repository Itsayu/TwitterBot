import tweepy
import time

consumer_key = 'KvANtIhF89JvRMxeyJFfKN2Av'
consumer_secret = 'CjXjIVevlu96LeVTyXkvlFuIweMAVBXAtFa2ymMKLpSYLqe5i3'
access_token = '1172074378353229824-Q5PNl31DHV7AC8HrChvFFtiFwztjNh'
access_token_secret = 'U2sJ9LGzbZPVV0EbBaYRtn5LI3T4bn7WFT6gvZ6eGDIXg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

hashtag = "100daysofcode"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()
