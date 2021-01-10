import tornado.httpserver
import tornado.ioloop
import tornado.web
import rsa
import json
import sys
from conv import *
from FlowData2Code import *
from SmartFlow import *
import subprocess
import os


def reload(sys):
	sys.setdefaultencoding('utf-8')

# from common import CustomStaticFileHandler
class PyCodeGenerator(tornado.web.RequestHandler):
    def post(self):
        myKey = self.get_argument("myKey", default="", strip=False)
        # create_graph is in conv.py
        graph = create_graph(json.loads(myKey))
        # create_code is in FlowData2Code.py
        create_code(graph)
        code = ''
        with open('generated_py.txt') as f:
            code = f.read()
        self.write(code)

# from common import CustomStaticFileHandler
class getSmartPreview(tornado.web.RequestHandler):
    def post(self):
        myKey = self.get_argument("myKey", default="", strip=False)
        # create_graph is in conv.py
        graph = create_graph(json.loads(myKey))
        # create_code is in FlowData2Code.py
        smart_preview(graph)
        code = ''
        with open('generated_smart_preview.txt') as f:
            code = f.read()
        self.write(code)

# from common import CustomStaticFileHandler
class smartExec(tornado.web.RequestHandler):
    def post(self):
        myKey = self.get_argument("myKey", default="", strip=False)
        # create_graph is in conv.py
        graph = create_graph(json.loads(myKey))
        # create_code is in FlowData2Code.py
        smart_exec(graph)
        code = ''
        with open('generated_smart_output.txt') as f:
            code = f.read()
        self.write(code)
        

class flow2code(tornado.web.RequestHandler):
    def get(self):
        self.render("IndexFlow2Code.html",error=None)

class smartFlow(tornado.web.RequestHandler):
    def get(self):
        self.render("IndexSmartFlow.html",error=None)

class execHandler(tornado.web.RequestHandler):
    def post(self):
        myKey = self.get_argument("myKey", default="", strip=False)
        graph = create_graph(json.loads(myKey))
        create_code(graph)
        with open("generated_py.txt") as f:
            if f.read().find('input()')>=0:
                self.write("#Cannot use \"input\" keyword when executing")
                return
        output = subprocess.check_output("python3 generated_py.txt", shell=True)
        self.write(output)

