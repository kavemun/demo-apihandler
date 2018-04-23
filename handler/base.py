import time
import tornado.ioloop
import tornado.web
import tornado.httpclient

class BaseHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        first_then = time.time()
        response = yield single_async_http_request()
        first_now = time.time()

        print("Single HTTP Request: %d" % round(first_now - first_then))
        print(response.body)

        second_then = time.time()
        future_a, future_b = yield [*multiple_async_http_requests()]
        second_now = time.time()

        print("Multiple HTTP Requests: %d" % round(second_now - second_then))
        print(future_a.body, future_b.body)
        print("Overall time: %d" % round(second_now - first_then))

        self.write('...')
        self.finish()


def multiple_async_http_requests():
    http = tornado.httpclient.AsyncHTTPClient()
    a = http.fetch("http://www.imdb.com")
    b = http.fetch("http://google.com")
    return a, b

@tornado.gen.coroutine
def single_async_http_request():
    http = tornado.httpclient.AsyncHTTPClient()
    response = yield http.fetch("http://www.yahoo.com")
    return response


default_handlers = [
    (r'/base', BaseHandler),
 ]
