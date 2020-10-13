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
print("show the five and recent tweets: \n")
i=1
for tweet in posts[0:5]:
    print(str(i) + ') '+ tweet.full_text + '\n')
    i=i+1
df=pd.DataFrame([tweet.full_text for tweet in posts],columns=['Tweets'])
df.head()


def cleanTxt(text):
    text=re.sub(r'@[A-Za-z0-9]+','',text)
    text=re.sub(r'#','',text)
    text=re.sub(r'RT[\s]+','',text)
    text=re.sub(r'https?:\/\/S+','',text)
    return text
df['Tweets']=df['Tweets'].apply(cleanTxt)
print(df)


def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity
df['Subjectivity']=df['Tweets'].apply(getSubjectivity)
df['Polarity']=df['Tweets'].apply(getPolarity)
print(df)

'''
allWords=' '.join([twts for twts in df['Tweets']])
wordCloud=WordCloud(width=500,height=300,random_state=21,max_font_size=119).generate(allWords)
plt.imshow(wordCloud,interpolation='bilinear')
plt.axis('off')
plt.show()
'''

def getAnalysis(score):
    if score<0:
        return 'Negative'
    elif score==0:
        return 'Neutral'
    else:
        return 'Positive'
df['Analysis']=df['Polarity'].apply(getAnalysis)
print(df)
