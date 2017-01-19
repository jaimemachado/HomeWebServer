from app import app
from flask_classy import FlaskView



class NotifyMyAndroidService(FlaskView):
    route_base = '/notifyandroid/';
    def test(self):
        return "test";
    def get(self):
        return "getTestAndroid";
    def index(self):
        return "Oi";


NotifyMyAndroidService.register(app);
