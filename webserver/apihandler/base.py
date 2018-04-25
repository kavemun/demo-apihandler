from tornado import web

from webserver.handler import BaseHandler

class APIHandler(BaseHandler):

   def get(self):
        self.write('.....')
        self.finish()

default_handlers = [
    (r'/apibase', APIHandler),
 ]