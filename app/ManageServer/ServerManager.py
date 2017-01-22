from app import app
from flask_classy import FlaskView
from app.Signals import restart_application2

class ServerManagerService(FlaskView):
    route_base = '/servermanager/';
    def restart(self):
        restart_application2.send()
        return "Oi";


ServerManagerService.register(app);