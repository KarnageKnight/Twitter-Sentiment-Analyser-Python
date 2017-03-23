import urllib
import json
import time

def countryFinder(address):
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    #print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    js1 = json.loads(data)
    #print 'Retrieved',len(data),'characters'
    #print json.dumps(js1,indent=4)
    if 'status' not in js1 or js1['status'] != 'OK':
        #print 'Failure To Retrieve'
        location='NA'
    elif js1['status']=='OVER_QUERY_LIMIT':
        time.sleep(0.5)
        location = countryFinder(address)
    else:
        for i in range(len(js1['results'][0]['address_components'])):
            if js1['results'][0]['address_components'][i]['types'][0]=="country":
                location = js1['results'][0]['address_components'][i]['long_name']
    #print location
    return location