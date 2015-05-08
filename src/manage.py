# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-25, by rory
# 
# 

__author__ = 'rory'

import os

from tornado.options import options, define
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import tornado.locale

from application import app
from config import BASE_DIR

define('port', default=8888, help='run on the given port', type=int)
# define('log_file_prefix', default=os.path.join(BASE_DIR, 'log/tornado.log'), help='define your own log file', type=str)

# xgettext -L python -k=_ -o tornado.po $(find . -name \*.py) $(find src/templates/ -name \*.html)


if __name__ == '__main__':
    tornado.options.parse_command_line()

    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)

    # 获取翻译
    tornado.locale.set_default_locale('zh_CN')
    tornado.locale.load_gettext_translations(os.path.join(BASE_DIR, 'locale'), 'tornado')

    print tornado.locale._supported_locales

    tornado.ioloop.IOLoop.instance().start()