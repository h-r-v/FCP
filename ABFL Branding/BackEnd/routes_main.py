import os
import rsa
import tornado.httpserver
import tornado.ioloop
import tornado.web
from admin_api import *
from settings import *
from tornado.web import url



if __name__ == "__main__":
    os.chdir('..')
    __file__ = str(os.getcwd()) + "/FrontEnd"
    
    app = tornado.web.Application(
    [
        (r'/flowchartgeneration', HomeHandler),
        (r'/getcode', PyCodeGenerator),
        (r'/execcode', execHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(__file__, 'static')}),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(__file__, 'static/')}),
    ],
    cookie_secret="46osdETzKXasdQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    template_path=__file__,
    debug = True,
    )

    app.rsa_keys = rsa.newkeys(1024)
    server = tornado.httpserver.HTTPServer(app)
    server.listen(Settings.port)
    print("Server running on port "+str(Settings.port))
    tornado.ioloop.IOLoop.current().start()
    print("Server stopped ...")
