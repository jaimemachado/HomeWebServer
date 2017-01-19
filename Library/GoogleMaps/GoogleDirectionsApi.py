from app import app
import googlemaps
from datetime import datetime



class GoogleMaps(object):
    def __init__(self):
        self.gmaps = googlemaps.Client(key = app.config['GOOGLE_KEY']);

    def GetLocation(self, address):
        return self.gmaps.geocode(address);

    def RequestRoute(self, origin, dest):
        return self.gmaps.directions(origin, dest);

