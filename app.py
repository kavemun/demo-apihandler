import time
import tornado.ioloop
import tornado.web
import tornado.httpclient

from handler import default_handlers

if __name__ == "__main__":
    app = tornado.web.Application(default_handlers)
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()