from tornado import web

from handler import BaseHandler

class APIHandler(BaseHandler):

   def get(self):
        self.write('...')
        self.finish()


