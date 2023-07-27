import tweepy
import time
import re 
from datetime import datetime, timedelta

consumer_key = 'RPFpvlz5YkdPEd2NGl9lWHJkg'
consumer_secret = 'LdhAweDBLm3OIPVj6BU1iaB6rIWBvyach77MNUzLwnBuZjLVvQ'
access_token = '1036468420361895937-VToQhzHnM04lmyZblLDp1n2XqPgUvs' 
access_token_secret = 'Yb33qZmUSptJ0Hj7U9aH2116JhDBmiom78zK7PHURnies' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def is_bot(username):
    try:
        user = api.get_user(username)
        bot_like_characteristics = 0

        # Criteria 1: Tweet perhari lebih dari 10
        tweets_per_day = user.statuses_count / ((time.time() - user.created_at.timestamp()) / (60 * 60 * 24))
        if tweets_per_day > 10:
            bot_like_characteristics += 1

        # Criteria 2: Perbandingan followers dan following 5:1
        if user.followers_count < user.friends_count / 5:
            bot_like_characteristics += 1

        # Criteria 3: Bio terlalu simple / kosong
        if user.description == "" or len(user.description.split(" ")) < 5:
            bot_like_characteristics += 1

        # Criteria 4: Username ada symbol atau angka
        if re.search(r'\d', username) or re.search(r'\W', username):
            bot_like_characteristics += 1

        # Criteria 5: Umur akun kurang dari 1 tahun
        if datetime.now() - user.created_at < timedelta(days=365):
            bot_like_characteristics += 1

        # Criteria 6: Tidak ada photo profile
        if user.default_profile_image:
            bot_like_characteristics += 1

        # Criteria 7: Memiliki jumlah retweet lebih dati 50 dalam seminggu
        retweets_last_week = 0
        one_week_ago = datetime.now() - timedelta(days=7)
        for status in tweepy.Cursor(api.user_timeline, id=username, tweet_mode="extended").items():
            if status.created_at < one_week_ago:
                break
            if hasattr(status, "retweeted_status"):
                retweets_last_week += 1
        if retweets_last_week > 50:
            bot_like_characteristics += 1

        if bot_like_characteristics >= 1:
            return True

        return False 

    except:
        print("Error processing account " + username)
        return False

username = "ClaudiaColiin"
print(is_bot(username))