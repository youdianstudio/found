#-*- coding:utf-8 -*-

from base import BaseHandler
import tornado.web

class HomeHandler(BaseHandler):
	
	@tornado.web.authenticated
	def get(self):
		self.render('home.html',user=self.current_user)
		
	@tornado.web.authenticated
	def post(self):
		pass


urls=[(r'/home',HomeHandler)]
