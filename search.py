from base import BaseHandler

class SearchHandler(BaseHandler):
	def get(self):
		keyword=self.get_argument('kw')
		self.write('you searched '+keyword)
	def post(self):
		pass
		
urls=[(r'/search',SearchHandler)]
