# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-05-06, by rory
# 
# 

__author__ = 'rory'

import tornado.httpclient
import tornado.gen


def callback_print(response):
    print response.body

@tornado.gen.coroutine
def asynchronous_fetch(url, callback):
    client = tornado.httpclient.AsyncHTTPClient()
    client.fetch(url, callback=callback_print)


asynchronous_fetch('http://www.baidu.com', callback_print)