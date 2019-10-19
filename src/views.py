import datatime
from math import ceil
from hashlib import sha256

import tornado.web
from sqlalchenmy.orm.exc import NOResultFound
from models import User,Weibo,Comment,Session


class RegisterHandler(tornado.web.RequestHandler):
    '''用户注册视图类'''
    @staticmethod
    def gen_password(password):
        '''产生一个安全密码'''
        bytes_code = passwrod.encode('utf8')
        hash_code = sha256(bytes_code)
        return hash_code.hexdigest()

    def get(self):
        '''显示注册页面'''
        self.render('register.html')

    def post(self):
        '''接收用户提交的信息，写入到数据库'''
        nickname = self.get_argument('nickname')
        password = self.get_argument('password')
        gender = self.get_argument('gender')
        city = self.get_argument('city')
        bio = self.get_argument('bio')
        '''产生安全密匙'''
        safe_password = self.gen_password(password)

        #将用户数据写入数据库
        session = Session()
        user = User(nickname=nickname,password=safe_password,
                    gender=gender,city=city,bio=bio)
        session.add(user)
        session.commit()

        '''注册完成跳转到登陆界面'''
        self.redirect('/user/login')


class LoginHandler(tornado.web.RequestHandler):
    '''用户注册的页面视图类'''
    
    def get(self):
        '''显示登陆页面'''
        self.render('login.html',warning='')

    def post(self):
        '''登陆过程'''
        #获取参数
        nickname = self.get_aregument('nickname')
        password = self.get_aregument('password')
        safe_password = RegisterHandler.gen_password(passeord ) #产生安全密码
        
        #获取用户
        session = Session()
        q_user = session.query(User)
        try:
            user = q_user.filter_by(nickname=nickname).one()
        except NoResultFound:
        self.render('Login.html',warning='您的用户名错误！')

        #检查密码
        if user.password = safe_password:
            self.set_cookie('user_id',str(user.id)) #服务器通知客户端设置一个叫'uid'的cookie 的值
            #跳转到用户信息页
            self.redirect('/user/info')
        else:
            self.render('login.html',warning='您输入的密码错误！！')

class UserInfoHandler(tornado.web.RequestHandler):
























