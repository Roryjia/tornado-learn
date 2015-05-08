# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-05-08, by rory
# 
# 

__author__ = 'rory'


from core.handler import BaseHandler


class LangHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.redirect('/')

    def post(self, *args, **kwargs):
        user_locale = self.get_argument('language')
        self.set_cookie('user_locale', user_locale)
        self.redirect(self.reverse_url('test-index'))
        # self.redirect('/test/index/')