#-*-coding:utf-8-*-

from tornado import  escape, ioloop
import os.path
import json
import tornado.web
from tornado.options import define, options
from models import createSession
from home import urls as homeurls
from search import urls as searchurls
from post import urls as posturls
from main import urls as  mainurls

define('port',default=8888,help='run on the given port',type=int)

class Application(tornado.web.Application):
	def __init__(self):
		handlers=posturls+homeurls+searchurls+mainurls
		settings=dict(
			cookie_secret='adsdfgdfharjwsewgf23435676ewjkdfrt',
			template_path=os.path.join(os.path.dirname(__file__),'templates'),
			static_path=os.path.join(os.path.dirname(__file__),'static'),
			login_url='/login',
			xsrf_cookies=True,
			#autoescape='xhtml_escape',
			autoescape=None,
			site_title='No Title',
			)
		tornado.web.Application.__init__(self,handlers,**settings)
		self.session=createSession()

def main():
	tornado.options.parse_command_line()
	app=Application()
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
if __name__=='__main__':
	main()
