#-*- coding:utf-8 -*-

from base import BaseHandler

class ErrorHandler(BaseHandler):
	def get(self):
		self.write('Error Occurred From Get !')
	def post(self):
		self.write('Error Occurred From Post !')
# ErrorHandler.urls must be at the end of all handler's urls
urls=[(r'/(.*)',ErrorHandler)]
