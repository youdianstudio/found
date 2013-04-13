#-*- coding:utf-8 -*-

from base import BaseHandler

class HomeHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect('/login')
			return
		else:
			pass	
	
	def post(self):
		pass


urls=[(r'/home',HomeHandler)]
