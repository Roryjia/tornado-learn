# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-25, by rory
# 
# 

__author__ = 'rory'

import tornado.web
import tornado.locale

from config import *

from core.ui import BaseUIModule

from auth.handler import MainHandler, LoginHandler
from test.handler import PageHandler, TestIndexHandler, TestPostHandler, TestUIModule, TestClientHandler
from lang.handler import LangHandler
from websocket.handler import SocketHandler, SocketTestHandler

UI_MODULES = {
    'Base': BaseUIModule,
    'Test': TestUIModule,
}

APPLICATION_SETTING.update(ui_modules=UI_MODULES)

app = tornado.web.Application([
    (r'^/?$', MainHandler),
    (r'^/login/?$', LoginHandler),

    (r'^/test/page/(\d+)/?$', PageHandler, {}, 'test-page'),
    (r'^/test/index/?$', TestIndexHandler, {}, 'test-index'),
    (r'^/test/post/?$', TestPostHandler),
    (r'^/test/client/?$', TestClientHandler),

    (r'^/i18n/set/?$', LangHandler),

    (r'^/socket/?$', SocketHandler),
    (r'^/socket/test/?$', SocketTestHandler),

], **APPLICATION_SETTING)