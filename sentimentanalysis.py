import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import csv
ConsumerKey = "5Wittq9oSwEecQrKo67RoGnZv"
ConsumerSecret = "cS6eAjrdFhRCLTjitROrLeNni2QHZRYjjsNutauaxxLywf33a0"
AccessToken = "221322633-AvWsANI3XXOqJP9hgI1TF6zgwWv6xU4uEXrBk2JL"
AccessTokenSecret = "ZfuCGRWvkVdkv6Vl4pngMf8u4zyByZuZwoQgOxOHt55M2"
authenticate = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
authenticate.set_access_token(AccessToken, AccessTokenSecret)
api = tweepy.API(authenticate, wait_on_rate_limit=True)
posts = api.user_timeline(screen_name="@RailMinIndia", count=100, lang="en", tweet_mode="extended")
print("show the five and recent tweets: \n")
i=1
for tweet in posts[0:5]:
    print(str(i) + ') '+ tweet.full_text + '\n')
    i=i+1
     # Stage 0- Importing Libraries and then setting keys for APIs
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


allWords=' '.join([twts for twts in df['Tweets']])
wordCloud=WordCloud(width=500,height=300,random_state=21,max_font_size=119).generate(allWords)
plt.imshow(wordCloud,interpolation='bilinear')
plt.axis('off')
plt.show()


def getAnalysis(score):
    if score<0:
        return 'Negative'
    elif score==0:
        return 'Neutral'
    else:
        return 'Positive'
df['Analysis']=df['Polarity'].apply(getAnalysis)
print(df)
#Stage 1: Cleaning data (Removing @,#,hyperlinks etc )

#print positive tweets

j=1
sortedDF=df.sort_values(by=['Polarity'])

for i in range(0,sortedDF.shape[0]):
    if sortedDF['Analysis'][i]=='Positive':
        print(str(j) + ') '+sortedDF['Tweets'][i])
        print()
        
        
        j=j+1
        



 #print all negative tweets
j=1
sortedDF=df.sort_values(by=['Polarity'],ascending='False')
for i in range(0,sortedDF.shape[0]):
    if(sortedDF['Analysis'][i]=='Negative'):
        print(str(j) + ')'+sortedDF['Tweets'][i])
        print()
        j=j+1
#plot polarity and subjectivity
plt.figure(figsize=(8,6))  
for i in range(0,df.shape[0]):
    plt.scatter(df['Polarity'][i],df['Subjectivity'][i],color='green')      
       
plt.title('Sentiment Analysis')  
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()   
 #get the percentage of positive tweets

ptweets=df[df.Analysis=='Positive']
ptweets=ptweets['Tweets']
print(round((ptweets.shape[0]/df.shape[0])*100,1))
   #get the percentage of negative tweets

ntweets=df[df.Analysis=='Negative']
ntweets=ntweets['Tweets']
print(round((ntweets.shape[0]/df.shape[0])*100,1))
#show the value counts iii8uyh
print(df['Analysis'].value_counts)
#plot and visualize counts
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('counts')
df['Analysis'].value_counts().plot(kind='bar')

plt.show()

#stage2 counting number of positive tweets and negative tweets,plotted graphs
<<<<<<< HEAD



#tweets = [{'sentiment' : 'positive', 'text' : 'some text'}, {'sentiment' : 'negative', 'text' : 'some other text'}]

#with open('tweets.csv', 'w') as csvfile:
 #   fieldnames = ['sentiment', 'text']
  #  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   # writer.writeheader()
    #writer.writerows(tweets)
=======
>>>>>>> 04908803d7bf7de958dc2f7e2112ed300b5e7eab
