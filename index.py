#-*-coding:utf-8-*-
import tornado.database
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import json

from tornado.options import define,options

from settings import *
from base import BaseHandler
from login import urls as loginurls
from home import urls as homeurls
from search import urls as searchurls

define('port',default=8888,help='run on the given port',type=int)

class Application(tornado.web.Application):
	def __init__(self):
		handlers=homeurls+loginurls+searchurls
		settings=dict(
			cookie_secret='adsdfgdfharjujaewsewgf2343567678gfdrewweewjkdfrt',
			template_path=os.path.join(os.path.dirname(__file__),'templates'),
			static_path=os.path.join(os.path.dirname(__file__),'static'),
			xsrf_cookies=True,
			#autoescape='xhtml_escape',
			autoescape=None
			)
		tornado.web.Application.__init__(self,handlers,**settings)

def main():
	tornado.options.parse_command_line()
	app=Application()
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
if __name__=='__main__':
	main()
