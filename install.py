#-*- coding:utf-8 -*-

import hashlib
import tornado.web

from base import BaseHandler
from models import User

class InstallHandler(BaseHandler):
	def get(self):
		table=self.session.query(Post)
		c=table.count()
		print c,'ccccc'
		if table.count()!=0:
			raise tornado.web.HTTPError(404)
		self.reander('install.html',usr=None,error=0)
	def post(self):
		usr=self.get_argument('usr',default=None)
		pwd=self.get_argument('pwd',default=None)
		nickname=self.get_argument('nickname',default=None)
		if not usr or not pwd:
			self.render('install.html',usr=usr,error=1)
		auth=hashlib.sha1(str(usr)+str(pwd)+'lostandfound').hexdigest()
		user=User()
		user.username=usr
		user.auth=auth
		user.nickname=nickname
		self.session.add(user)
		self.session.commit()
		self.redirect('login')
urls=[('r/install',InstallHandler)]
