import requests
from datetime import datetime
from mapquest_key import mapquest_key
from geocode import geocode
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#import key. This key needs to be in a `mapquest_key.py` file in the path

#inx = input('Enter location: ')
inx = 'Rougemont%2C+Switzerland'
# make a dict with our parameters 
params = {
    mapquest_key,
    inx    
}

result1=geocode(mapquest_key, inx) # here we get a dict 
#maps=requests.get("http://open.mapquestapi.com/geocoding/v1/address", params=params)
print(result1.items) # here we need to have the keys and values enumerated 
geocode_result=maps.json()
print(geocode_result)
print('Formatted Address: ' + geocode_result['results'][0]['providedLocation']['location'])
latx=geocode_result['results'][0]['location'][0]['latLng']['lat']
lonx=geocode_result['results'][0]['location'][0]['latLng']['lng']

iss_next_pass = requests.get("http://api.open-notify.org/iss-pass.json", {"lat": latx, "lon": lonx})
print()
t = datetime.fromtimestamp(float(iss_next_pass.json()['response'][0]['risetime']))

print('Next Viewing Opportunity: ') 
print(t) 
#+ ', duration: ') #+ iss_next_pass.json()['response'][0]['duration'])
