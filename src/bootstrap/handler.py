# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-05-10, by rory
# 
# 

__author__ = 'rory'


from core.handler import BaseHandler


class BootstrapFirstHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('bootstrap/first.html')