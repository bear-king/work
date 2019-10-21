#!/usr/bin/env python

import tornado.web
import tornado.ioloop
from tornado.options import parse_command_line

import views

route = [
        (r'/user/register',views.RegisterHandler),
        (r'/user/login',views.LoginHandler),
        (r'/user/info',views.UserInfoHandler),
        ]
web_app = tornado.web.Application(
        route,
        template_path = 'templates',
        static_path = 'statics',
        )
parse_command_line()
web_app.listen(8000,'0.0.0.0')
print('Server running on 0.0.0.0:8000')
tornado.ioloop.IOLoop.current().start()
