from util.jsonify import jsonify
from util.elro import Elro


class Plug:
    exposed = True
     
    def __init__(self):
      self.states = [
          1,
          0
      ]
      self.elro = Elro();
    
    
    @jsonify
    def GET(self, id=-1):
        return self.states
    
    @jsonify
    def POST(self, id, body=None):
        id = int(id);
        newState= (self.states[id] -1) * -1;
        print("switching plug " + str(id+1) + " to state " + str(newState));
        self.elro.switch(id, newState);
        self.states[id] = newState;
        return newState