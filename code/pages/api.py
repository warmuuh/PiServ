import cherrypy
from .gpio import Gpio
from .bash import Bash
from .plug import Plug
class Api:
    gpio = Gpio()
    bash = Bash()
    plug = Plug()
    
    