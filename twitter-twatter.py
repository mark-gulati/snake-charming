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

results = twitter.search(q = "pylint")

print(type(results))
print(results)
