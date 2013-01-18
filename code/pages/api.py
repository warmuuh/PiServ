import cherrypy
from .gpio import Gpio
class Api:
    gpio = Gpio()
    
    