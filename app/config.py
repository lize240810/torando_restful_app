# -*- coding: utf-8 -*-

import os
from tornado.options import define, options

# 监听端口
define(
    "port",
    default=8999,
    help="端口运行",
    type=int
)

# 配置
settings = {
    'debug': True,
    'static_path': os.path.join(os.getcwd(), 'static'),
    'template_path': os.path.join(os.getcwd(), 'templates'),
}