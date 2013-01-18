from util.jsonify import jsonify
from .GpioState import GpioState


class Gpio:
    exposed = True
     
    def __init__(self):
      self.states = [
      GpioState(1),
      GpioState(0),
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(1),
      
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(0),
      GpioState(1),
      GpioState(1)
      ]
    
    
    @jsonify
    def GET(self, id=-1):
        return self.states
    
    @jsonify
    def POST(self, id, body=None):
        id = int(id);
        print("switching pin " + str(id+1) + " to state " + str(body.state));
        self.states[id].state = body.state;
    