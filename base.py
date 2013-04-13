#-*- coding:utf-8 -*-

import tornado.web

from models import User

class BaseHandler(tornado.web.RequestHandler):
	@property
	def session(self):
		return self.application.session
	
	def write_error(self,status_code):
		print ' In write_error :',status_code
		if status_code in [403,404,500,503]:
			self.write('Error %s' % status_code)
		else:
			self.write('BOOM!')
		
		
	def get_current_user(self):
		auth=self.get_secure_cookie('auth')
		if not auth:
			return None
		query=self.session.query(User).filter_by(auth=auth)
		print ' get_current_user executed'
		if query.count==0:
			return None
		return query.one()
		#return self.get_secure_cookie('user')
