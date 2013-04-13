#-*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker,relationship,backref
import datetime
from sqlalchemy 	import *
from sqlalchemy.ext.declarative import declarative_base,declared_attr

from config import *

connectionString="mysql://%s:%s@%s:%s/%s?charset=utf8" \
				%(MYSQL_USER,MYSQL_PASS,MYSQL_HOST,str(MYSQL_PORT),MYSQL_DB)
'''
create an engine maintains a pool of connection
'''
engine=create_engine(connectionString,echo=False,encoding='utf8',convert_unicode=True)
Base=declarative_base()

'''
define the table 'user' in the database and map it to class 'User' 
'''
class User(Base):
	__tablename__='user'
	#__table_args__={'mysql_engine':'InnoDB'}
	id=Column(Integer,primary_key=True)
	name=Column(String(40),nullable=False,unique=True)
	nickname=Column(String(40),nullable=False,unique=True)
	auth=Column(String(50),nullable=False,unique=True)
	#posts=relationship('Post',backref='poster')
	created=Column(DateTime,nullable=False,default=datetime.datetime.now())
	updated=Column(DateTime,nullable=False,default=datetime.datetime.now())
	
	def __init__(self,name,nickname,auth,created):
		self.name=name
		self.nickname=nickname
		self.auth=auth
		self.created=created
		self.updated=created
		
	def __repr__(self):
		return 'User<%d,%s,%s>' %(self.id,self.name,self.nickname)
		
class Post(Base):

	__tablename__='post'
	#__table_args__={'mysql_engine':'InnoDB'}
	id=Column(Integer,primary_key=True)
	title=Column(String(100))
	content=Column(String(500))
	poster_id=Column(Integer,ForeignKey('user.id'),nullable=False)
	#poster=relationship('User',back_populated='posts')
	poster=relationship('User',backref='posts')
	created=Column(DateTime,nullable=False)
	updated=Column(DateTime,nullable=False)
	
	def __init__(self,title,content,created):
		self.title=title
		self.content=content
		self.created=created
		self.updated=created
	def __repr__(self):
		return 'Post<%d,%s>' %(self.id,self.title)
		 		
Base.metadata.create_all(engine)# create the defined tables
'''
we communicate with the database by  session
'''
def createSession():
	Session=sessionmaker(bind=engine)
	session=Session()
	return session


