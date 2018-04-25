import json
import sys
import logging

from .base import APIHandler
from _version import __version__

from webserver.modelserver import ModelServer

from urllib.parse import unquote

class DeployModelHandler(APIHandler):

   def get(self):
        logging.info('TODO: Deploy Model Handler.')
        self.finish()

class UpdateModelHandler(APIHandler):

   def get(self):
        self.write('TODO: Update Model')
        self.finish()


class PredictHandler(APIHandler):

   def get(self):
        self.write('TODO: for Making Prediction')
        self.finish()


class MyHandler(APIHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="POST">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self, filename):
        filename = unquote(filename)
        mtype = self.request.headers.get('Content-Type')
        logging.info('POST "%s" "%s" "%s" ', filename, mtype, self.get_body_argument("message")) 
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))


class User(APIHandler):
    def get(self):
        form = """<form method="post">
        <input type="text" name="username"/>
        <input type="text" name="designation"/>
        <input type="submit"/>
        </form>"""
        self.write(form)

    def post(self, filename="test"):
        username = self.get_argument('username')
        designation = self.get_argument('designation')
        self.write("Wow " + username + " you're a " + designation + " with a " + filename)

default_handlers = [
    (r'/api/model/deploy', DeployModelHandler),
    (r'/api/model/update', UpdateModelHandler),
    (r'/api/model/predict', PredictHandler),
    (r'/api/model/test', MyHandler),
    (r'/user', User),
]