from subprocess import call

class Elro:
     
    def __init__(self):
      return;
    
    
   
    def switch(self, id, on):
        if on:
            return self.switchOn(id);
        else:
            return self.switchOff(id);
        
    def switchOn(self, id):
        call(["/home/pi/prog/funk/elro_wiring.py",""+id,"1"])
        return True;
    
    def switchOff(self, id):
        call(["/home/pi/prog/funk/elro_wiring.py",str(pow(2,id)),"0"])
        return True;
    