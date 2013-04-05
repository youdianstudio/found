#-*-coding:utf-8-*-
import tornado.database
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import json

from tornado.options import define,options
from base import BaseHandler
from login import urls as loginurls
from home import urls as homeurls

define('port',default=8888,help='run on the given port',type=int)

MYSQL_DB='found'
MYSQL_HOST='127.0.0.1'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASS='zcj'
class Application(tornado.web.Application):
	def __init__(self):
		handlers=homeurls+loginurls
		settings=dict(
			cookie_secret='adsdfgdfharjujaewsewgf2343567678gfdrewweewjkdfrt',
			template_path=os.path.join(os.path.dirname(__file__),'templates'),
			static_path=os.path.join(os.path.dirname(__file__),'static'),
			xsrf_cookies=True,
			#autoescape='xhtml_escape',
			autoescape=None
			)
		tornado.web.Application.__init__(self,handlers,**settings)
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		mdb =tornado.database.Connection("%s:%s"%(MYSQL_HOST,str(MYSQL_PORT)), MYSQL_DB,MYSQL_USER, MYSQL_PASS)
		query='select name from kw '
		results=mdb.query(query)
		#encodedjson=json.dumps(results,ensure_ascii=False,indent=4)
		print type(results)
		#results=[{'name':u'钱包'}]
		#results=[u'钱包']
		print results
		#self.write(encodedjson)
		self.render('index.html',keywords=results)
		
	
	def post(self):
		pass

def main():
	tornado.options.parse_command_line()
	app=Application()
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
if __name__=='__main__':
	main()
