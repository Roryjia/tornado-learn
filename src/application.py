# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-25, by rory
# 
# 

__author__ = 'rory'

import tornado.web

from config import *

from core.ui import BaseUIModule

from auth.handler import MainHandler, LoginHandler
from test.handler import PageHandler, TestIndexHandler, TestPostHandler, TestUIModule, TestClientHandler

UI_MODULES = {
    'Base': BaseUIModule,
    'Test': TestUIModule,
}

APPLICATION_SETTING.update(ui_modules=UI_MODULES)

app = tornado.web.Application([
    (r'^/?$', MainHandler),
    (r'^/login/?$', LoginHandler),
    (r'^/test/page/(\d+)/?$', PageHandler),
    (r'^/test/index/?$', TestIndexHandler),
    (r'^/test/post/?$', TestPostHandler),
    (r'^/test/client/?$', TestClientHandler),
], **APPLICATION_SETTING)