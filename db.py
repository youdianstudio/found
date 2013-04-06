#-*- coding:utf-8 -*-

from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import *

DBSession=sessionmaker(autoflush=True,expire_on_commit=False)

def ConnectDB():
	ConnectString='mysql://%s:%s@%s/%s?charset=utf8' %(MYSQL_USER,
				MYSQL_PASS,MYSQL_HOST,MYSQL_DB)

	engine=create_engine(ConnectString,encoding='utf8',convert_unicode=True)
	DBSession.configure(bind=engine)
	session=DBSession()
	return session
