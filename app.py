import time
import tornado.ioloop
import tornado.web
import tornado.httpclient

from handler import BaseHandler
from apihandler import APIHandler

from handler import default_handlers


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/foo/?", default_handlers),
    ])
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()