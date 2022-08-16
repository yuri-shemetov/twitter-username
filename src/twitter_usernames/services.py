import tweepy
import pandas as pd

from proj import local_settings


api_key = local_settings.API_KEY
api_key_secret = local_settings.API_SECRET_KEY
access_token = local_settings.API_ACCESS_TOKEN
access_token_secret = local_settings.API_ACCESS_TOKEN_SECRET
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_followers(username):
    api.get_user(screen_name=username).followers_count
    return api.get_user(screen_name=username).followers_count


def get_following(username):
    return api.get_user(screen_name=username).friends_count


def get_description(username):
    return api.get_user(screen_name=username).description


def get_10_tweets(username, limit=10):
    columns = ["Date", "Tweet"]
    data = []
    tweets = api.user_timeline(screen_name=username, count=limit, tweet_mode="extended")
    for tweet in tweets:
        data.append([tweet.created_at, tweet.full_text])
    df = pd.DataFrame(data, columns=columns)

    return df["Tweet"]
