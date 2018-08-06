# Python app to log on to Twitter and parse your favorites

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

searchstr = "demi lovato"

results = twitter.search(q = searchstr)

#'screen_name': 'pythonvscode'
print(type(results)) # it is a <class 'dict'>
 
print(results)
print("Writing results to file...")
filename = searchstr+'-search.json'
with open(filename, 'w') as outfile:
  outfile.write(json.dumps(results, indent=4)) #dump as string because we are opening file as 'w' not 'wb'

print("Now starting for loop...")

i = 0
print("Number of posts found: ", len(results['statuses'])) 
for i in range(0,len(results['statuses'])):
    print(results['statuses'][i])
    print(results['statuses'][i]['entities'])
    print(results['statuses'][i]['entities']['urls'])
#twitter.update_status(status="Nice day today...")


print("Exiting...")