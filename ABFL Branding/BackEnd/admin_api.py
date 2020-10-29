import tornado.httpserver
import tornado.ioloop
import tornado.web
import rsa
import json
import sys
from conv import *
from FlowData2Code import *
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

        

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("Index.html",error=None)

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

