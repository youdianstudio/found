#-*- coding:utf-8 -*-
# create ,edit or delete a post 

import datetime
import tornado.web
from sqlalchemy import desc
from tornado.web import authenticated
from base import BaseHandler
from models import Post

#create a new post
class NewPostHandler(BaseHandler):

	@authenticated
	def get(self):
		self.render('newpost.html',title=None,content=None,error=0)
		
	@authenticated
	def post(self):
		title=self.get_argument('title',default='No Title')
		content=self.get_argument('content',default=None)
		if not content:
			self.render('newpost.html',title=title,content=content,error=1)#content can't be empty
			return
		elif not title:
			self.render('newpost.html',title=title,content=content,error=2)# title can't be empty
			return			
		user=self.current_user
		print user
		user.posts.append(Post(title,content,datetime.datetime.now()))
		#self.session.add(user)
		#self.session.commit()
		self.redirect('/home')

#view the detail of the post		
class PostDetailHandler(BaseHandler):
	def get(self,id):
		post=self.session.query(Post).get(id)
		if not post:
			raise tornado.web.HTTPError(404)
		self.render('postdetail.html',post=post)

#edit a post		
class EditPostHandler(BaseHandler):

	@tornado.web.authenticated
	def get(self,id):
		post=self.session.query(Post).get(id)
		if not post:
			raise tornado.web.HTTPError(404)
		self.render('editpost.html',post=post)
		
	@tornado.web.authenticated
	def post(self,id):
		post=self.session.query(Post).get(id)
		if not post:
			raise tornado.web.HTTPError(404)
		title=self.get_argument('title',default='No Title')
		content=self.get_argument('content',default=None)

		self.redirect('/post/'+str(id))
		
#delete a post
class DeletePostHandler(BaseHandler):

	@tornado.web.authenticated
	def get(self,id):
		post=self.session.query(Post).get(id)
		if not post:
			raise tornado.web.HTTPError(404)
		self.render('deletepost.html',post=post)
		
	@tornado.web.authenticated
	def post(self,id):
		post=self.session.query(Post).get(id)
		self.session.delete(post)
		self.session.commit()
		self.redirect('/home')

urls=[(r'/new',NewPostHandler),
		(r'/post/([^/]+)',PostDetailHandler),
		(r'/post/([^/]+)/edit',EditPostHandler),
		(r'/post/([^/]+)/remove',DeletePostHandler)
		]
	
	
