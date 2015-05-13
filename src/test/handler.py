# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-03-25, by rory
# 
# 

__author__ = 'rory'

import json
import os

import tornado.httpclient
import tornado.web

from core.handler import BaseHandler
from core.ui import BaseUIModule
from config import BASE_DIR


class TestUIModule(BaseUIModule):
    """
    测试嵌入js/css
    """

    def embedded_javascript(self):
        return u'alert("你进去了这里哦!")'

    def embedded_css(self):
        css = 'h1 {background-color:#F5F5F5}' \
              '.container p {background-color:#555}'
        return css

    def css_files(self):
        return ['css/test.css', ]

    def javascript_files(self):
        return ['js/test/test.js', ]

    def render(self, *args, **kwargs):
        return self.render_string('test/embed.html', books=['Python', 'Tornado', 'Django'])


class PageHandler(BaseHandler):
    """
    测试 url 参数匹配
    """
    def get(self, *args, **kwargs):
        print args
        print kwargs
        self.write('hello {0}'.format(args[0]))


class TestIndexHandler(BaseHandler):
    """
    加载模版
    """
    def get(self, *args, **kwargs):
        # q = self.get_argument('q')

        self.render('test/index.html')


class TestPostHandler(BaseHandler):
    """
    处理 test index form post
    """
    def post(self, *args, **kwargs):
        image = self.request.files.get('image')
        if image:
            filename = image[0].get('filename')
            with open(os.path.join(BASE_DIR, 'media', filename), 'wb') as f:
                f.write(image[0].get('body'))
                f.close()

        print image
        print type(image)
        print image[0].keys()

        name1 = self.get_argument('name1')
        name2 = self.get_argument('name2')
        name3 = self.get_arguments('name3')
        ctx = {
            'name1': name1,
            'name2': name2,
            'name3': name3,
            'books': ['Python', 'Tornado', 'Django'],
        }
        self.render('test/show.html', **ctx)


class TestClientHandler(BaseHandler):
    """
    测试 tornado http client 模块，以及json数据的返回。
    """
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        # client = tornado.httpclient.HTTPClient()

        client = tornado.httpclient.AsyncHTTPClient()
        try:
            client.fetch('http://dev.api.mezone.me/v3/business/business/itravel/nearby/?platform=a&button=MS&page=1',
                         callback=self.on_response)
        except Exception, e:
            print e, type(e)

    def on_response(self, response):
        # print response.__dict__, dir(response)

        # print type(response.body)
        self.write(response.body)
        self.finish()