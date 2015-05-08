# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-25, by rory
# 
# 

__author__ = 'rory'

import tornado.escape

from core.handler import BaseHandler


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        if not self.current_user:
            self.redirect('/login')
            return

        # 为未解码前字符串
        # self.write(self.get_cookie('user'))
        name = tornado.escape.xhtml_escape(self.current_user)
        # print self.get_query_arguments('name') --> []
        self.write('welcome to  {name}'.format(name=name))
        # self.flush()


class LoginHandler(BaseHandler):
    def get(self):
        self.render('auth/login.html')

    def post(self):
        self.set_secure_cookie('user', self.get_argument('name', 'rory'))
        self.redirect('/')