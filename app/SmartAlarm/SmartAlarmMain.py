import json

from flask import request
from flask_classy import FlaskView
from Library.GoogleMaps.GoogleDirectionsApi import GoogleMaps
from app import app


class SmartAlarmService(FlaskView):
    route_base = '/smartalarm/';
    def __init__(self):
        self.maps = GoogleMaps();

    def getlocation(self):
        temp = self.maps.GetLocation(request.headers.get('Location'));
        #directions = self.maps.RequestRoute(tempParsed[0]['formatted_address'], tempParsed2[0]['formatted_address'])
        return json.dumps(temp);
    def get(self):
        return "getTest";
    def index(self):
        return "Oi";


SmartAlarmService.register(app);
