# Python app to log on to Twitter and parse your favorites

from twython import Twython
import psycopg2
import urllib3
import twitter_secret

twitter_credentials = twitter_secret.twitter_credentials

twitter = Twython(twitter_credentials['consumer_api_key'],
  twitter_credentials['consumer_secret_key'],
  twitter_credentials['access_token'],
  twitter_credentials['token_secret'])

results = twitter.search(q = "demi lovato")
#'screen_name': 'pythonvscode'
print(type(results)) # it is a <class 'dict'>
i = 0
print("Number of posts found: ", len(results['statuses']))
for i in range(0,len(results['statuses'])):
    print(results['statuses'][i]['entities'])
    print(results['statuses'][i]['entities']['urls'])
twitter.update_status(status="Nice day today...")
print("Exiting...")