import json
import requests

def geocode(mapquest_key, inx):
    result = {}
    url = 'http://open.mapquestapi.com/geocoding/v1/address?key={0}&location={1}'

    request = url.format(mapquest_key, inx)
    maps = json.loads(requests.get(request).text)

    if len(maps['results']) > 0:
        result = maps['results'][0]
    else:
        result={}
    return result
