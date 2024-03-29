'''
This code fetches tweets from various accounts,
stores them in a variety of useful formats as desired,
verifies whether or not they have the same content.
and then tweets them accordingly.

It is a general purpose machine that can adapt to any type 
of twitter content. This set of tools relies not only on tweepy,
but on twitter itself, making it highly dependent on a volatile
platform.
'''

import tweepy
import time

#API keys on your account
consumer_key="H1mQSNPlrV6Gx05l1PAqyhPuZ"
consumer_secret="gyxcRYbattTU1u1PFPlLbTot7xryXcNuxcsKJvpyQ3qNHxW1Bc"
access_token="1170277041222115328-DTKCIRu07nUzUb1nt6cQs19G5mIPOx"
access_secret="n9tXsh4jUKh7yY3UWp37kWXPALBMPu1JkeA7NLAiLBHQb"

#sign in on your account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#initialise variables globally
source_tweets = []
tweets_to_post = []

print('\n')
print('\n')
print('\n')
print('###############LOOKUP_USERS###############')

print(api.lookup_users(screen_names=['tix', 'xy', 'abc']))
print('\n')
print('\n')
print('\n')

print('###############GET_USER###############')

print(api.get_user(screen_name='tix'))
print('\n')
print('\n')
print('\n')

print('###############SEARCH_USERS###############')

print(api.search_users('tix'))
print('\n')
print('\n')
print('\n')

def tweet_get(screen_name):
    
    tweets = []	
    
    print("Fetching tweets from", screen_name)
    
    new_tweets = api.user_timeline(screen_name = screen_name,count=10) #get 10 recent tweets
    
    #extend is important here
    tweets.extend(new_tweets)
        
    source_tweets = [tweet.text for tweet in tweets]
    
    #put all the tweets into one list to be posted as a single tweet
    tweets_to_post.append(source_tweets)
    

print('\n')

tweet_get("tix")
'''
tweet_get("cnn")
tweet_get("nytimes")
tweet_get("theeconomist")
tweet_get("reuters")
tweet_get("wsj")
tweet_get("time")
tweet_get("abc")

tweet_get("washingtonpost")
tweet_get("bbcbreaking")
tweet_get("ajenews")
tweet_get("nowthisnews")
tweet_get("telegraph")
tweet_get("bbc")
tweet_get("skynews")
tweet_get("afp")
tweet_get("channel24")
tweet_get("ewnupdates")
tweet_get("nbcnews")
tweet_get("msnbc")
tweet_get("business")
tweet_get("cbsnews")
tweet_get("itvnews")
tweet_get("techcrunch")
tweet_get("guardian")
tweet_get("forbes")
tweet_get("ap")
tweet_get("financialtimes")
tweet_get("independent")
tweet_get("huffpost")
'''

#####################################################################
print('\n')
print(tweets_to_post)
print('\n')

big_list = []
for strings in tweets_to_post:
    #print(strings[0]) #pure string form of each tweet
    list_strings = strings[0].split() #each word in list form
    big_list.append(list_strings) #form a list from each loop iteration

total = []
for i in big_list: #merge sublists!
    total += i

print(total)
print('\n')

def headline_match(total, query): #see if a specific query appears twice
    i = 0
    matches = []
    for item in total:
        if item == query:
            matches.append(i)
            i += 1
    for i in matches[1:]: #only print matches greater than 0
        print(str(matches) + " " + query)

for loops in range(len(total)): #repeat function for each word in total
    headline_match(total, total[loops])

#tweet on your account
#api.update_status(tweets)
