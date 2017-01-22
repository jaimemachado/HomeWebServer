import json

from flask import request
from flask_classy import FlaskView
from Library.GoogleMaps.GoogleDirectionsApi import GoogleMaps
from app import app
from app.Signals import restart_application2

class SmartAlarmService(FlaskView):
    route_base = '/smartalarm/';

    def restartWebServer2(self):
        print "REBOOT SIGNAL RECEIVED2"
        #self.reboot = True;

    def __init__(self):
        self.maps = GoogleMaps();

        def handle_restartWebServer2(sender, **kwargs):
            self.restartWebServer2();
        self.handle_restartWebServer2 = handle_restartWebServer2;
        restart_application2.connect(handle_restartWebServer2);

    def getlocation(self):
        temp = self.maps.GetLocation(request.headers.get('Location'));
        #directions = self.maps.RequestRoute(tempParsed[0]['formatted_address'], tempParsed2[0]['formatted_address'])
        return json.dumps(temp);
    def get(self):
        return "getTest";




SmartAlarmService.register(app);
