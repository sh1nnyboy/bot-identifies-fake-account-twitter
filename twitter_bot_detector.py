import tweepy
import time
import re
from datetime import datetime

# Insert your Twitter API credentials here
consumer_key = 'insert your api key'
consumer_secret = 'insert your api secret'
access_token = 'insert your access token' 
access_token_secret = 'insert your access token secret' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def is_bot(username):
    try:
        user = api.get_user(screen_name=username)
        bot_like_characteristics = 0

        # Criterion 1: More than 10 tweets per day
        tweets_per_day = user.statuses_count / ((time.time() - user.created_at.timestamp()) / (60 * 60 * 24))
        if tweets_per_day > 10:
            bot_like_characteristics += 1

        # Criterion 2: Followers to following ratio less than 1:5
        if user.followers_count < user.friends_count / 5:
            bot_like_characteristics += 1

        # Criterion 3: Bio too simple or empty
        if user.description == "" or len(user.description.split(" ")) < 3:
            bot_like_characteristics += 1

        # Criterion 4: Username contains symbols or numbers
        if re.search(r'\d', username) or re.search(r'\W', username):
            bot_like_characteristics += 1

        # Criterion 5: No profile picture
        if user.default_profile_image:
            bot_like_characteristics += 1

        # Criterion 6: Account age less than one year
        account_age_days = (datetime.now() - user.created_at).days
        if account_age_days < 365:
            bot_like_characteristics += 1

        # Criterion 7: No profile banner
        try:
            banner = user.profile_banner_url
        except Exception:
            bot_like_characteristics += 1

        # Criterion 8: Follows one of these political accounts (if you want to check other political accounts, you can change the target_accounts list)
        target_accounts = ['aniesbaswedan', 'prabowo', 'ganjarpranowo']
        target_ids = [api.get_user(screen_name=target).id for target in target_accounts]
        following_ids = api.friends_ids(user.id)
        if any(target_id in following_ids for target_id in target_ids):
            bot_like_characteristics += 1

        # Account is considered a bot if it meets 5 or more criteria
        if bot_like_characteristics >= 5:
            return True

        return False 

    except Exception as e:
        print(f"Error processing account {username}")
        print(f"Exception: {e}")
        return False

def main():
    username = input("Enter Twitter username to check: ")
    bot_result = is_bot(username)

    if bot_result:
        print(f"Bot: {username}")
    else:
        print(f"Human: {username}")

if __name__ == "__main__":
    main() 