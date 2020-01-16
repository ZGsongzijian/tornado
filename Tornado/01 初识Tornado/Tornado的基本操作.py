'''安装 Tornado'''
# 以管理员身份运行CMD : pip install tornado==4.3


'''示例: 你好世界'''
# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/index", MainHandler),
#     ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)    # 监听端口
#     tornado.ioloop.IOLoop.current().start()

'''示例: 用户登录'''
# import tornado.ioloop
# import tornado.web
#
# settings = {
#     'template_path': 'templates'  # 指定模板地址[模板默认在根目录下]
# }
#
# # 成功登录后程序
# class Success_Handler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("恭喜登录成功")
#
# # 用户登录程序
# class Unsrname_Handler(tornado.web.RequestHandler):
#     def get(self):
#         self.render('login.html', msg='')
#
#     def post(self, *args, **kwargs):
#         user = self.get_body_argument('user')
#         pwd = self.get_body_argument('pwd')
#         if user == 'alex' and pwd == '123':
#             self.redirect('/index')
#         else:
#             self.render('login.html', msg='用户密码错误')
#
# def make_app():
#     return tornado.web.Application([
#         (r"/index", Success_Handler),
#         (r"/login", Unsrname_Handler),
#     ], **settings)
#
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)  # 监听端口
#     tornado.ioloop.IOLoop.current().start()

'''示例: 返回连续问题: finish() '''
# import tornado.ioloop
# import tornado.web
#
# settings = {
#     'template_path':'templates'   # 指定模板地址[模板默认在根目录下]
# }
#
# # 成功登录后程序
# class Success_Handler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("恭喜登录成功")
#         self.write('123')   # 两个 write连在一块 返回为： 恭喜登录成功123
#         self.finish()       # 完成write 不在写入数据  456不会出现在页面中
#         self.write('456')
#
# # 用户登录程序
# class Unsrname_Handler(tornado.web.RequestHandler):
#     def get(self):
#         self.render('login.html',msg='')
#
#     def post(self,*args,**kwargs):
#         user = self.get_body_argument('user')
#         pwd = self.get_body_argument('pwd')
#         if user == 'alex' and pwd == '123':
#             self.redirect('/index')
#         self.render('login.html',msg='用户密码错误')
#
# def make_app():
#
#     return tornado.web.Application([
#         (r"/index", Success_Handler),
#         (r"/login", Unsrname_Handler),
#     ],**settings)
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)    # 监听端口
#     tornado.ioloop.IOLoop.current().start()

'''示例: 模板语法问题(使用的python语句,不需要特定的语法) 与 静态文件缓存'''
# import tornado.ioloop
# import tornado.web
#
# settings = {
#     'template_path': 'templates',  # 指定模板地址[模板默认在根目录下]
#     'static_path': 'static',  # 指定资源地址  只要文件中出现 {{ static_url('静态文件') }} 的字样,就必须指定static的地址
# }
#
# # 浏览器 /static/commons.css?v=26e9bc16f81da955b429ff6a2b6e617d
# # 浏览器 /static/commons.css?v=bb4e7e0a75ce164a478e4f51bea597b0  缓存地址
#
# # 成功登录后程序
# class Success_Handler(tornado.web.RequestHandler):
#     def get(self):
#         user_dict = [
#             {'id': 1, 'name': '应用'},
#             {'id': 2, 'name': '名称'},
#             {'id': 3, 'name': 'IE'},
#             {'id': 4, 'name': '问问'},
#             {'id': 5, 'name': 'wt'},
#         ]
#         # self.render('index.html', users=user_dict)
#         self.render('index.html', **{'users':user_dict})
#
# # 用户登录程序
# class Unsrname_Handler(tornado.web.RequestHandler):
#     def get(self):
#         self.render('login.html', msg='')
#
#     def post(self, *args, **kwargs):
#         user = self.get_body_argument('user')
#         pwd = self.get_body_argument('pwd')
#         if user == 'alex' and pwd == '123':
#             self.redirect('/index')
#         else:
#             self.render('login.html', msg='用户密码错误')
#
#
# def make_app():
#     return tornado.web.Application([
#         (r"/index", Success_Handler),
#         (r"/login", Unsrname_Handler),
#     ], **settings)
#
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)  # 监听端口
#     tornado.ioloop.IOLoop.current().start()

'''示例: cookie问题--cookie的设置和获取'''
# import tornado.ioloop
# import tornado.web
#
# settings = {
#     'template_path': 'templates',  # 指定模板地址[模板默认在根目录下]
#     'static_path': 'static',  # 指定资源地址  只要文件中出现 {{ static_url('静态文件') }} 的字样,就必须指定static的地址
#     'cookie_secret': 'jia_mi',  # 加密cookie的秘钥
# }
#
# # 成功登录后程序
# class Success_Handler(tornado.web.RequestHandler):
#     def get(self):
#         # 获取 cookie
#         print(self.get_cookie('k1'))
#         print(self.get_secure_cookie('k2'))  # 在控制台显示字节类型,但是在浏览器是另一种类型
#
#         user_dict = [
#             {'id': 1, 'name': '应用'},
#             {'id': 2, 'name': '名称'},
#         ]
#         self.render('index.html', **{'users': user_dict})
#
# # 用户登录程序
# class Unsrname_Handler(tornado.web.RequestHandler):
#     def get(self):
#         self.render('login.html', msg='')
#
#     def post(self, *args, **kwargs):
#         user = self.get_body_argument('user')
#         pwd = self.get_body_argument('pwd')
#         if user == 'alex' and pwd == '123':
#             # 设置 cookie
#             self.set_cookie('k1', 'asasasa')  # 明文cookie
#             self.set_secure_cookie('k2', user)  # 加密cookie
#
#             # 返回重定向
#             self.redirect('/index')
#         else:
#             self.render('login.html', msg='用户密码错误')
#
#
# def make_app():
#     return tornado.web.Application([
#         (r"/index", Success_Handler),
#         (r"/login", Unsrname_Handler),
#     ], **settings)
#
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)  # 监听端口
#     tornado.ioloop.IOLoop.current().start()

'''示例: cookie问题--大批量设置cookie 和 没有登录不让访问 '''
# 在 tornado 中: 装饰器可以,  没有中间件 , 可以重写源码【编写一个基类，让登录者继承基类】
import tornado.ioloop
import tornado.web

settings = {
    'template_path': 'templates',  # 指定模板地址[模板默认在根目录下]
    'static_path': 'static',  # 指定资源地址  只要文件中出现 {{ static_url('静态文件') }} 的字样,就必须指定static的地址
    'cookie_secret': 'jia_mi',  # 加密cookie的秘钥
}

# 编写cookie基类
class AuthHandler(tornado.web.RequestHandler):
    def prepare(self):
        user_session = self.get_secure_cookie('user_session_id')
        if user_session:
            return None
        self.redirect('/login')

# 成功登录后程序
class Success_Handler(AuthHandler):
    def get(self):
        user_dict = [
            {'id': 1, 'name': '应用'},
            {'id': 2, 'name': '名称'},
        ]
        self.render('index.html', **{'users': user_dict})

# 用户登录程序
class Unsrname_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html', msg='')

    def post(self, *args, **kwargs):
        user = self.get_body_argument('user')
        pwd = self.get_body_argument('pwd')
        if user == 'alex' and pwd == '123':
            # 设置 cookie
            self.set_secure_cookie('user_session_id', user)  # 加密cookie

            # 返回重定向
            self.redirect('/index')
        else:
            self.render('login.html', msg='用户密码错误')


def make_app():
    return tornado.web.Application([
        (r"/index", Success_Handler),
        (r"/login", Unsrname_Handler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # 监听端口
    tornado.ioloop.IOLoop.current().start()
