import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
ConsumerKey = "5Wittq9oSwEecQrKo67RoGnZv"
ConsumerSecret = "cS6eAjrdFhRCLTjitROrLeNni2QHZRYjjsNutauaxxLywf33a0"
accessToken = "221322633-AvWsANI3XXOqJP9hgI1TF6zgwWv6xU4uEXrBk2JL"
accessTokenSecret = "ZfuCGRWvkVdkv6Vl4pngMf8u4zyByZuZwoQgOxOHt55M2"
authenticate = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
authenticate.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(authenticate, wait_on_rate_limit=True)
posts = api.user_timeline(screen_name="@RailMinIndia", count=100, lang="en", tweet_mode="extended")
print("show the five recent tweets: \n")
for tweet in posts[0:5]:
    print(tweet.full_text + '\n')
