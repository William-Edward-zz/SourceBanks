import tweepy
import time

#API keys on your account
consumer_key=""
consumer_secret=""
access_token=""
access_secret=""

#sign in on your account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#initialise variables globally
source_tweets = []
tweets_to_post = []

def tweet_get(screen_name):
    
    tweets = []	
    
    print("Fetching tweets from", screen_name)
    
    new_tweets = api.user_timeline(screen_name = screen_name,count=1)
    
    #extend is important here
    tweets.extend(new_tweets)
        
    source_tweets = [[tweet.text] for tweet in tweets]
    
    #for i in source_tweets[0]:
    #    tweet_string = i
    #    print(tweet_string)
    
    #put all the tweets into one list to be posted as a single tweet
    tweets_to_post.append(source_tweets)
    

print('\n')
tweet_get("cnn")
tweet_get("foxnews")
tweet_get("nytimes")
tweet_get("theeconomist")
tweet_get("reuters")
tweet_get("wsj")
tweet_get("time")
tweet_get("abc")
tweet_get("washingtonpost")
tweet_get("bbcbreaking")
print('\n')

print(tweets_to_post)

#tweet on your account
#api.update_status(tweets)
