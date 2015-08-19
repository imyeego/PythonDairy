###################
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# Author: liuzhao
# Date:2015-08-19
###################
import os.path
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index1.html")

handlers = [
	(r"/", MainHandler),
]
template_path = os.path.join(os.path.dirname(__file__),"templates")

if __name__ =="__main__":
	app = tornado.web.Application(handlers, template_path)
	http_server = HTTPServer(app)
	app.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
