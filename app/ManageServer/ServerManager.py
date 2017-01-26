from app import app
from flask_classy import FlaskView
from app.Signals import restart_application2

class ServerManagerService(FlaskView):
    route_base = '/servermanager/';
    def alive(self):
        return "ALIVE";


ServerManagerService.register(app);