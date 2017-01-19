from app import app
from flask_classy import FlaskView



class SmartAlarmService(FlaskView):
    route_base = '/smartalarm/';
    def test(self):
        return "test";
    def get(self):
        return "getTest";
    def index(self):
        return "Oi";


SmartAlarmService.register(app);
