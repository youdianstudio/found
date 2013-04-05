from base import BaseHandler
import tornado.database
from settings import *
class MainHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect('/login')
			return
		mdb =tornado.database.Connection("%s:%s"%(MYSQL_HOST,str(MYSQL_PORT)), MYSQL_DB,MYSQL_USER, MYSQL_PASS)
		query='select name from kw '
		results=mdb.query(query)
		#encodedjson=json.dumps(results,ensure_ascii=False,indent=4)
		#self.write(encodedjson)
		self.render('index.html',keywords=results)
		
	
	def post(self):
		pass


urls=[(r'/',MainHandler)]
