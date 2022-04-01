# import tweepy
# import time
#
# consumer_key = 'KvANtIhF89JvRMxeyJFfKN2Av'
# consumer_secret = 'CjXjIVevlu96LeVTyXkvlFuIweMAVBXAtFa2ymMKLpSYLqe5i3'
# access_token = '1172074378353229824-Q5PNl31DHV7AC8HrChvFFtiFwztjNh'
# access_token_secret = 'U2sJ9LGzbZPVV0EbBaYRtn5LI3T4bn7WFT6gvZ6eGDIXg'
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
# FILE_NAME = 'last_seen.txt'
#
# def read_last_seen(FILE_NAME):
#     file_read = open(FILE_NAME, 'r')
#     last_seen_id = int(file_read.read().strip())
#     file_read.close()
#     return last_seen_id
#
# def store_last_seen(FILE_NAME, last_seen_id):
#     file_write = open(FILE_NAME, 'w')
#     file_write.write(str(last_seen_id))
#     file_write.close()
#     return
#
# def reply():
#     tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
#     for tweet in reversed(tweets):
#         if '#aktweet' in tweet.full_text.lower():
#             print("Replied To ID - " + str(tweet.id))
#             api.update_status("@" + tweet.user.screen_name + " Good Luck For #100DaysOfCode!", tweet.id)
#             api.create_favorite(tweet.id)
#             api.retweet(tweet.id)
#             store_last_seen(FILE_NAME, tweet.id)
#
# while True:
#     reply()
#     time.sleep(15)

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
