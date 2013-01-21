#todo: serve static files  (http://docs.cherrypy.org/stable/progguide/files/static.html)

import cherrypy
import os.path





#tmpl = env.get_template('index.html')
#        return tmpl.render(salutation='Hello', target='Wodrld', name=name)



from jinja2 import Environment, FileSystemLoader
from util.jinja2plugin import Jinja2TemplatePlugin
env = Environment(loader=FileSystemLoader('templates'))
Jinja2TemplatePlugin(cherrypy.engine, env=env).subscribe()

# Register the Jinja2 tool
from util.jinja2tool import Jinja2Tool
cherrypy.tools.template = Jinja2Tool()









from pages import * 

current_dir = os.getcwd()
userpassdict = {'pi' : 'serv'}
checkpassword = cherrypy.lib.auth_basic.checkpassword_dict(userpassdict)
cherrypy.config.update("config.cfg")
conf = {
  '/': {
        'tools.auth_basic.on': True,
        'tools.auth_basic.realm': 'piserv',
        'tools.auth_basic.checkpassword': checkpassword,
        
        'tools.staticdir.on': True,
        'tools.staticdir.dir': current_dir,
        'tools.encode.on': False
  },
  '/api' : {
     'request.dispatch': cherrypy.dispatch.MethodDispatcher()
  }
}  

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(index.PageController(), '/', config=conf)

