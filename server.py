#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpclient
from pymmseg import mmseg

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("Hello, world")
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://friendfeed-api.com/v2/feed/bret", callback=self.on_response)

    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + str(len(json["entries"])) + " entries from the FriendFeed API")
        self.finish()

class SegmentHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def post(self):
        keyword = self.get_argument('keyword')
        algor = mmseg.Algorithm(keyword.encode('utf-8'))
        ret = []
        for tok in algor:
            ret.append({'start' : tok.start})
            ret.append({'end' : tok.end})
            ret.append({'length' : tok.length})
            ret.append({'text' : tok.text.decode('utf-8')})
        self.write(tornado.escape.json_encode(ret))
        self.finish()

mmseg.dict_load_defaults()

application = tornado.web.Application([
    (r"/test", MainHandler),
    (r"/segment", SegmentHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
