# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-25, by rory
# 
# 

__author__ = 'rory'

import os

from core.handler import Handler404

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


TEMPLATES_PATH = os.path.join(BASE_DIR, 'templates')
STATIC_PATH = os.path.join(BASE_DIR, 'static')

DEFAULT_HANDLER_CLASS = Handler404


APPLICATION_SETTING = {
    'debug': True,
    'cookie_secret': "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    'template_path': TEMPLATES_PATH,
    'static_path': STATIC_PATH,
    'xsrf_cookies': True,
    'login_url': '/login/',
    'default_handler_class': DEFAULT_HANDLER_CLASS
}