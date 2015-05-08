# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-25, by rory
# 
# 

__author__ = 'rory'


from tornado.options import options, define
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web

from application import app

define('port', default=8888, help='run on the given port', type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()

    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()