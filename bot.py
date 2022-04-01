import time

import tweepy

consumer_key = 'KvANtIhF89JvRMxeyJFfKN2Av'
consumer_secret = 'CjXjIVevlu96LeVTyXkvlFuIweMAVBXAtFa2ymMKLpSYLqe5i3'
access_token = '1172074378353229824-Q5PNl31DHV7AC8HrChvFFtiFwztjNh'
access_token_secret = 'U2sJ9LGzbZPVV0EbBaYRtn5LI3T4bn7WFT6gvZ6eGDIXg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# api.update_status('Hey Folks...!')

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


# -----------REPLY TO THE MENTIONED TWEET (USING THE FILE 'last_seen.txt')------------
FILE_NAME = 'last_seen.txt'


# for tweet in tweets:
#     if '#aktweet' in tweet.text:
#         print("New Tweet Found!")
#         print(str(tweet.id) + ' - ' + tweet.text)

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#aktweet' in tweet.full_text.lower():
            print("Replied To ID - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " Good Luck For #DOntquIT!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(15)

# ---------------USE TO DISPLAY THE ID OF THE TWEET (THE ID WHICH ARE MENTION IN THE FILE i.e., last_seen.txt)---------
# id = read_last_seen(FILE_NAME)
# print(id)

# tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
# for tweet in tweets:
#     if '#aktweet' in tweet.full_text.lower:
#         print("New Tweet Found!")
#         print(str(tweet.id) + ' - ' + tweet.full_text)
#
#         store_last_seen(FILE_NAME, tweet.id)
#
#         # print(str(tweet.id) + ' - ' + tweet.full_text)



