# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-05-08, by rory
# 
# 

__author__ = 'rory'

import tornado.websocket

from core.handler import BaseHandler


class SocketHandler(tornado.websocket.WebSocketHandler):
    """
    web socket test
    """
    def open(self):
        print 'web socket is opened'

    def on_message(self, message):
        self.write_message('Your said : ' + message)

    def on_close(self):
        print 'web socket is closed'


class SocketTestHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('socket/socket.html')