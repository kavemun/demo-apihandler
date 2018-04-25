import time
import tornado.ioloop
import tornado.web
import tornado.httpclient

from webserver.handler import default_handlers
from webserver.apihandler import default_handlers as api_handlers

if __name__ == "__main__":
    default_handlers.extend(api_handlers)
    app = tornado.web.Application(default_handlers)
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()