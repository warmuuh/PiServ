import json
import importlib
import functools
import cherrypy


class jsonify( object ):
  def __init__(self,f):
    self.f = f
    
  def dict_to_object(self, d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        #module = __import__(module_name)
        module = importlib.import_module(module_name)
        #print ('MODULE:', module)
        class_ = getattr(module, class_name)
        #print ('CLASS:', class_)
        args = dict( (key, value) for key, value in d.items())
        #print ('INSTANCE ARGS:', args)
        inst = class_(**args)
    else:
        inst = d
    return inst
  
  def convert_to_builtin_type(self, obj):
    # Convert objects to a dictionary of their representation
    d = { '__class__':obj.__class__.__name__, 
          '__module__':obj.__module__,
          }
    d.update(obj.__dict__)
    return d
  
  def addBody(self, kwargs):
     nkwargs = {}
     nkwargs.update(kwargs)
     objStr = cherrypy.request.body.read().decode('utf-8');
     #print("PARAM: " + objStr)
     nkwargs["body"] = json.loads(objStr, object_hook=self.dict_to_object)
     return nkwargs
  
  def __call__(self, *args, **kwargs ):
   
    if cherrypy.request.body.length is not None:
      kwargs = self.addBody(kwargs)
    
    results = self.f( *args, **kwargs)
    j = json.dumps( results, default=self.convert_to_builtin_type ).encode("utf-8")
    return j
    
    
  def __get__(self, instance, instancetype):
    """Implement the descriptor protocol to make decorating instance 
    method possible."""
    
    # Return a partial function with the first argument is the instance 
    #   of the class decorated.
    return functools.partial(self.__call__, instance) 
  
