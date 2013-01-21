import cherrypy
from .gpio import Gpio
from .bash import Bash
class Api:
    gpio = Gpio()
    bash = Bash()
    
    