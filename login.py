from base import BaseHandler

class LoginHandler(BaseHandler):
	def get(self):
		self.render('login.html',dict=None)
	def post(self):
		name=self.get_argument('name')
		print name,'name'
		self.set_secure_cookie('user',self.get_argument('name'))
		self.redirect('/')
		
urls=[(r'/login',LoginHandler)]
