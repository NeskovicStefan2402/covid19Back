from geopy.geocoders import Nominatim
from urllib.request import urlopen
import json
import reverse_geocoder as rg
class Lokacija():
    @classmethod
    def vrati_drzavu(cls,data):
        koordinate=str(data['lat'])+' , '+str(data['lng'])
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.reverse("44 , 45")
        reci=location.address.split(',')
        return reci[-1]

    @classmethod
    def vratiKoordinate(cls,drzava):
        try:
            geolocator = Nominatim(user_agent="my_app")
            location = geolocator.geocode(drzava)
            return [location.latitude,location.longitude]
        except:
            return [0,0]

    @classmethod    
    def getplace(cls,lat, lon):
        url = "http://maps.googleapis.com/maps/api/geocode/json?"
        url += "latlng=%s,%s&sensor=false"%  (lat, lon)
        v = urlopen(url).read()
        j = json.loads(v)
        components = j['results'][0]['address_components']
        country = town = None
        for c in components:
            if "country" in c['types']:
                country = c['long_name']
            if "postal_town" in c['types']:
                town = c['long_name']
        return country

