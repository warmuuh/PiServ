import cherrypy
from .api import Api

class PageController:
    api=Api()
    
    
    @cherrypy.expose
    @cherrypy.tools.template(template='status.html')
    def index(self, name=None):
        return  {"cpu":{'usage':'65',
                        'processes':'30'}}
    
    @cherrypy.expose
    @cherrypy.tools.template(template='gpio.html')
    def gpio(self, name=None):
        return  {}
    
    @cherrypy.expose
    @cherrypy.tools.template(template='house.html')
    def house(self, name=None):
        return  {}
    