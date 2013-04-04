import tornado.database
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import json
from tornado.options import define,options

define('port',default=8888,help='run on the given port',type=int)

MYSQL_DB='menagerie'
MYSQL_HOST='127.0.0.1'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASS='zcj'
class Application(tornado.web.Application):
	def __init__(self):
		handlers=[
			(r'/',MainHandler)
			]
		settings=dict(
			cookie_secret='adsdfgdfharjujaewsewgf2343567678gfdrewweewjkdfrt',
			template_path=os.path.join(os.path.dirname(__file__),'templates'),
			static_path=os.path.join(os.path.dirname(__file__),'static'),
			xsrf_cookies=True,
			autoescape='xhtml_escape',
			)
		tornado.web.Application.__init__(self,handlers,**settings)
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		mdb =tornado.database.Connection("%s:%s"%(MYSQL_HOST,str(MYSQL_PORT)), MYSQL_DB,MYSQL_USER, MYSQL_PASS)
		query='select * from pet '
		results=mdb.query(query)
		#encodedjson=json.dumps(results,ensure_ascii=False,indent=4)
		
		#self.write(encodedjson)
		self.render('index.html',results=results)
		
	
	def post(self):
		pass

def main():
	tornado.options.parse_command_line()
	app=Application()
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
if __name__=='__main__':
	main()
