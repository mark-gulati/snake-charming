# Read a JSON file, Connect to RDS and write it to a table 

import psycopg2
import json

# read the file
with open('subscriptions.json','r') as infile:
    subscriptions = json.load(infile)

#print(subscriptions)
#print(type(subscriptions)) # dict
for i in range(0, len(subscriptions)):
    print("subscription_id: ",subscriptions['response'][i]['subscription']['id'])