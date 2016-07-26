# -*- coding: UTF-8 -*-

import urllib,urllib2,json

# baidu api's url
url = 'http://api.map.baidu.com/geocoder/v2/?ak=xjtZZGL1SeNud97uRBjfwMr1&output=json&'

def getlocation(addr,city=None):
    if city is None:
        params = ({'address':addr.encode('utf-8')})
    else:
        params = ({'address':addr.encode('utf-8'),'city':city.encode('utf-8')})
    getString=url+urllib.urlencode(params)
    
    responseJson = urllib2.urlopen(getString)
    resLocation = json.loads(responseJson.read())
    location = resLocation['result']['location']
    return location
    
        
    
    
    

