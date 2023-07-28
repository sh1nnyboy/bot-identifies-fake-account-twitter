import tweepy
import time
import re
from datetime import datetime

# Insert your own consumer_key, consumer_secret, access_token, and access_token_secret
consumer_key = 'diUncxIseQPJQjnA9KgvL6pmt'
consumer_secret = 'fc9CxWLGUdHIh8EJHApGvPc61g9xQFacDAlOVxmjrNHTcKuEpK'
access_token = '1334183299015606272-b8w3RcYqXldAk6OOG2Ux2UJgzIZchx' 
access_token_secret = 'gwgnuZEfRdbmpy4dqtdMVD5YLuunySXyIIJiQR3VNATF5' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def is_bot(username):
    try:
        user = api.get_user(screen_name=username)
        bot_like_characteristics = 0

        # Criteria 1: Tweet perhari lebih dari 10
        tweets_per_day = user.statuses_count / ((time.time() - user.created_at.timestamp()) / (60 * 60 * 24))
        if tweets_per_day > 10:
            bot_like_characteristics += 1

        # Criteria 2: Perbandingan followers dan following 5:1
        if user.followers_count < user.friends_count / 5:
            bot_like_characteristics += 1

        # Criteria 3: Bio terlalu simple / kosong
        if user.description == "" or len(user.description.split(" ")) < 3:
            bot_like_characteristics += 1

        # Criteria 4: Username ada symbol atau angka
        if re.search(r'\d', username) or re.search(r'\W', username):
            bot_like_characteristics += 1

        # Criteria 5: Tidak ada photo profile
        if user.default_profile_image:
            bot_like_characteristics += 1

        # Criteria 6: Umur akun kurang dari satu tahun
        account_age_days = (datetime.now() - user.created_at).days
        if account_age_days < 365:
            bot_like_characteristics += 1

        # Criteria 7: Tidak memiliki banner
        try:
            banner = user.profile_banner_url
        except Exception:
            bot_like_characteristics += 1

        # Criteria 8: Follow salah satu dari @aniesbaswedan, @prabowo, @ganjarpranowo
        target_ids = [api.get_user(screen_name=target).id for target in ['aniesbaswedan', 'prabowo', 'ganjarpranowo']]
        following_ids = api.friends_ids(user.id)
        if any(target_id in following_ids for target_id in target_ids):
            bot_like_characteristics += 1

        if bot_like_characteristics >= 5:
            return True

        return False 

    except Exception as e:
        print("Error processing account " + username)
        print("Exception:", e)
        return False

username = "username"
bot_result = is_bot(username)

if bot_result:
    print("Bot: " + username)
else:
    print("Human: " + username)
