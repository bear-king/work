#!/usr/bin/env python

import tornado.web
import tornado.ioloop
import tornado.option import pase_command_line

import views

route = [
        (r'/user/register',Views.RegisterHandler),
        (r'/user/login',Views.LoginHandler),
        (r'/user/info',Views.UserInfoHandler),

        (r'/weibo/post',Views.PostWeiboHandler),
        (r'/weibo/show',Views.ShowWeiboHandler),

        (r'/comment/commit',Views.CommentCommitHandler),
        (r'/comment/reply',Views.ComentReplyHandler),
        ]
web_app = tornado.web.Applicatin(
        route,
        template_path = 'templates',
        static_path = 'statics',
        )
parse_command_line()
web_app.listen(8000,'0.0.0.0')
print('Server running on 0.0.0.0:8000')
tornado.ioloop.IOLoop.current().start()
