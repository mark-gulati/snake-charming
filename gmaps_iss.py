import requests
import googlemaps
from datetime import datetime
import gmaps_api_key


gmaps_key=gmaps_api_key.gmaps_key #import key. This key needs to be in a `gmaps_api_key.py` file in the path

gmaps=googlemaps.Client(key=gmaps_key)
inx = input('Enter location: ')

geocode_result=gmaps.geocode(inx)
print('Formatted Address: ' + geocode_result[0]['formatted_address'])
latx=geocode_result[0]['geometry']['location']['lat']
lonx=geocode_result[0]['geometry']['location']['lng']

iss_next_pass = requests.get("http://api.open-notify.org/iss-pass.json", {"lat": latx, "lon": lonx})
print()
t = datetime.fromtimestamp(float(iss_next_pass.json()['response'][0]['risetime']))

print('Next Viewing Opportunity: ') 
print(t) 
#+ ', duration: ') #+ iss_next_pass.json()['response'][0]['duration'])
