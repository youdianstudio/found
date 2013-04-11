#-*- coding:utf-8 -*-

from sqlalchemy.orm import mapper,sessionmaker
from datetime       import datetime
from sqlalchemy 	import *
from sqlalchemy.ext.declarative import declarative_base

from config import *

connectionString="mysql://%s:%s@%s:%s/%s?charset=utf8" \
				%(MYSQL_USER,MYSQL_PASS,MYSQL_HOST,str(MYSQL_PORT),MYSQL_DB)
engine=create_engine(connectionString,echo=True,encoding='utf8',convert_unicode=True)
metadata=MetaData()
Base=declarative_base()
user_table=Table(
	'user',metadata,
	Column('id',Integer,primary_key=True),
	Column('name',String(40),unique=True,nullable=False),
	Column('auth',String(50),unique=True,nullable=False),
	Column('nickname',String(50),unique=True,nullable=true,default='Unknown'),
	Column('created',DateTime,default=datetime.now),
	Column('updated',DateTime,nullable=True)
	)
metadata.create_all(engine)

class User(Base):
	__tablename__='user'
	id=Column(Integer,primary_key=True)
	name=Column(String(40))
	auth=Column(String(50))
	created=Column(DateTime)
	def __init__(self):
		pass

	def __repr__(self):
		return 'User Table'
		
#mapper(User,user_table)
Session=sessionmaker()
Session.configure(bind=engine)
session=Session()
u=User()
u.name='hello'
u.auth='hello1234545'
session.add(u)
session.flush()
session.commit()
query=session.query(User)
print list(query)
