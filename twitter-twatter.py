# Python app to log on to Twitter and parse your favorites
# https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/ (uses tweepy)

from twython import Twython
import psycopg2
import urllib3
import twitter_secret
import json

twitter_credentials = twitter_secret.twitter_credentials

twitter = Twython(twitter_credentials['consumer_api_key'],
  twitter_credentials['consumer_secret_key'],
  twitter_credentials['access_token'],
  twitter_credentials['token_secret'])

faves = twitter.get_favorites() #gets 20 by default. <class 'list'>

print(type(faves)) # it is a <class 'list'>
 
print(faves)

print("Writing results to file...")
with open('faves.json', 'w') as outfile:
  outfile.write(json.dumps(faves, indent=4)) #dump as string because we are opening file as 'w' not 'wb'

print("Now starting for loop...")

i = 0
print("Number of posts found: ", len(faves)) 
for i in range(0,len(faves)):
    print(faves[i])
    print(faves[i]['entities']['media'])
    print(faves[i]['entities']['media'][0]['media_url'])
    print(faves[i]['entities']['urls'])


print("Exiting...")