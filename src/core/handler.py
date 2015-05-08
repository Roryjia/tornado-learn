# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-25, by rory
# 
# 

__author__ = 'rory'

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """
    base request handler class
    """
    def data_received(self, chunk):
        pass

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def write_error(self, status_code, **kwargs):
        # if status_code not in ['200', 200, 0, '0']:
        # print status_code
        # print kwargs
        self.set_status(200)
        return self.render('main/error.html', status_code=status_code, **kwargs)

    def get_browser_locale(self, default='zh_CN'):
        return super(BaseHandler, self).get_browser_locale(default=default)


class Handler404(BaseHandler):
    def get(self, *args, **kwargs):
        self.send_error(404)