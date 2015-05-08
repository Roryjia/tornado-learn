# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-27, by rory
# 
# 

__author__ = 'rory'

import tornado.web


class BaseUIModule(tornado.web.UIModule):
    """
    测试 UI Module
    """
    def render(self, *args, **kwargs):
        return u'<h1>Hello 渴了小屋<h1>'