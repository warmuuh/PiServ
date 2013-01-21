import cherrypy
from .api import Api

class PageController:
    api=Api()
    
    
    @cherrypy.expose
    @cherrypy.tools.template(template='status.html')
    def index(self):
        return  {"cpu":{'usage':'65',
                        'processes':'30'}}
    
    @cherrypy.expose
    @cherrypy.tools.template(template='gpio.html')
    def gpio(self):
        return  {}
    
    
    @cherrypy.expose
    @cherrypy.tools.template(template='bash.html')
    def bash(self):
        return  {}
        
        
    @cherrypy.expose
    @cherrypy.tools.template(template='house.html')
    def house(self):
        return  {}
    