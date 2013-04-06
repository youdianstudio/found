#-*- coding:utf-8 -*-

from sqlalchemy import *
from sqlalchemy.orm import relation
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import *

ConnectString='mysql://%s:%s@%s/%s?charset=utf8' %(MYSQL_USER,
				MYSQL_PASS,MYSQL_HOST,MYSQL_DB)

engine=create_engine(ConnectString,encoding='utf8',convert_unicode=True)
#metadata=MetaData()
#metadata.create_all(engine)
Base=declarative_base()
metadata=Base.metadata
KW_Table=Table('kw',metadata,
				Column('id',Integer,primary_key=True),
				Column('name',String(30)),
				mysql_charset='utf8')
Content_Table=Table('content',metadata,
				Column('id',Integer,primary_key=True),
				Column('title',String(100)),
				Column('content',String(500)),
				Column('author_id',Integer,ForeignKey('user.id'),
				Column('publishtime',DATETIME),
				Column('updatetime',DATETIME),
				mysql_charset='utf8')
User_Table=Table('user',metadata,
				Column('id',Integer,primary_key=True),
				Column('username',String(40)),
				Column('auth',String(40)),
				Column('nickname',String(40)),
				mysql_charset='utf8')

				
metadata.create_all(engine)

class KeyWord(Base):
	__tablename__='kw'
	id=Column(Integer,primary_key=True,autoincrement=True)
	name=Column(String)
	def __init__(self,name):
		self.name=name
	def __repr__(self):
		#return "<Kw('%s')>",%(self.name)
		return 'KW'
class Content(Base):
	__tablename__='content'
	id=Column(Integer,primary_key=True,autoincrement=True)
	title=Column(String)
	content=Column(String)
	author_id=Column(Integer,ForeignKey('user.id'))
	author=relation('user',lazy='immediate',order_by='user.id')
	publishtime=Column(DATETIME)
	updatetime=Column(DATETIME)
	def __init__(self,title,content,author_id,publishtime,updatetime):
		self.title=title
		self.content=content
		self.author_id=author_id
		self.publishtime=publishtime
		self.updatetime=updatetime
	def __repr__(self):
		return "<Content('%s','%s','%d','%s','%s')>" \
		%(self.title,self.content,self.author_id,self.publishtime,self.updatetime)
class User(Base):
	__tablename__='user'
	id = Column(Integer, primary_key = True,autoincrement=True)
	username = Column(String)
	auth = Column(String)
	nickname = Column(String)
	def __init__(self,username,auth,nickname):
		self.username=username
		self.auth=auth
		self.nickname=nickname
	def __repr(self):
		return "User"
	
