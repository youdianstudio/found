from base import BaseHandler

class LoginHandler(BaseHandler):
	def get(self):
		self.render('login.html',dict=None)
	def post(self):
		name=self.get_argument('name')
		print name,'name'
		self.set_secure_cookie('user',self.get_argument('name'),expires_days=7)
		self.redirect('/')

class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_all_cookies()
		self.redirect('/')
	def post(self):
		pass
		
urls=[(r'/login',LoginHandler),(r'/logout',LogoutHandler)]
