from util.jsonify import jsonify
from .CmdOutput import CmdOutput
import os
import subprocess
import sys

class Bash:
    exposed = True
 
    def __init__(self):
      self.cwd = os.getcwd()
    
    @jsonify
    def GET(self, id=-1):
        return CmdOutput( self.cwd + ">", "", "", "")
    
    @jsonify
    def POST(self, body=None):
        p = subprocess.Popen(body.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=".")# close_fds=True) #close_fds for linux only
        output, errors = p.communicate()
        
        return CmdOutput(self.cwd + ">", body.cmd, output.decode(sys.stdout.encoding), errors.decode(sys.stdout.encoding))  #"windows-1252" on windows