# -*- coding: utf-8 -*-
'''
	数据库
'''
import pymongo
from pymongo import MongoClient


# mongodb的连接配置
py_client = MongoClient('localhost', 27017)
# 创建一个数据库
db = py_client["demo"]
# py_client.list_database_names()