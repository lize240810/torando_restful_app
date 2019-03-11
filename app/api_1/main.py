# -*- coding: utf-8 -*-
'''
    主入口
'''
import datetime

import tornado.web
from tornado.httpserver import HTTPServer  # 服务web模块的加单http服务
import tornado.ioloop  # 核心的 I/O 循环


from .blog import BlogHandler, MainHandler
from app.config import *


def main():
    # 注册路由
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/blog", BlogHandler),
    ], **settings)
    # 实例化 http_server
    http_server = HTTPServer(application)
    # 绑定监听端口
    http_server.bind(tornado.options.options.port)
    # 多任务执行
    http_server.start(1)
    # 开启
    tornado.ioloop.IOLoop.instance().start()
