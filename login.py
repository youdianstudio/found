#-*- coding:utf-8 -*-

import hashlib
import tornado.web
from sqlalchemy import desc

from base import BaseHandler
from models import User

class LoginHandler(BaseHandler):
	def get(self):
		if self.current_user:
			self.redirect('/')
			return 0
		self.render('login.html',usr=None,error=0)
	def post(self):
		if self.current_user:
			self.redirect('/')
		usr=self.get_argument('usr',default=None)
		pwd=self.get_argument('pwd',default=None)
		if not usr or not pwd:
			self.render('login.html',usr=usr,error=1)
			return
		auth=hashlib.sha1(str(usr)+str(pwd)+'lostandfound').hexdigest()
		query=self.session.query(User).filter_by(auth=auth)
		if query.count()==0:
			self.render('login.html',usr=usr,error=2)
			return
		print name,'name'
		self.set_secure_cookie('auth',auth,expires_days=21)# the cookie expires in 21 days
		self.redirect('/')

class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie('auth')
		self.redirect('/')
	def post(self):
		pass
		
urls=[(r'/login',LoginHandler),(r'/logout',LogoutHandler)]
