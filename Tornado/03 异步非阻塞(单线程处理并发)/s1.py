import tornado.ioloop
import tornado.web


'''注意事项:'''
    # 异步:  体现在回调函数
    # 非阻塞:  体现在两方面[ 用户不用等待, socket程序不用等待]

'''流程:'''
    # IO多路复用监听socket列表 [服务端socket, 客户端socket, 为客户端向地方发送网络请求创建socket]
    # 为客户端向地方发送网络请求创建socket 结果返回后,自动执行Futrue的 set_result
    # IO多路复用的循环检测到Future对象发生变化. 就要调用客户端socket  为客户端返回信息



'''示例: 正常请求下,阻塞【等待处理完第一个，就处理下一个】'''
# import requests
# class index_Handler(tornado.web.RequestHandler):
#     def get(self):
#         value = self.get_query_argument('v')    # URL上的参数 v： 访问时访问 http://127.0.0.1:8888/index?v= XXX
#         print('请求来了',value)
#
#         # 访问第三方依次是: 必应  百度  谷歌
#         # ret = requests.get('https://cn.bing.com/',params={'value':value})
#         ret = requests.get('https://www.baidu.com/',params={'value':value})
#         # ret = requests.get('https://www.google.com.hk/',params={'value':value})
#
#         print('请求回来了',value,ret)
#         self.write('完成')
#
# def make_app():
#     return tornado.web.Application([
#         (r"/index", index_Handler),
#     ], )
#
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)  # 监听端口
#     tornado.ioloop.IOLoop.current().start()

'''示例:异步非阻塞 != 获取结果'''
# from tornado import httpclient
# from tornado import gen
#
#
# class index_Handler(tornado.web.RequestHandler):
#
#     @gen.coroutine
#     def get(self):
#         value = self.get_query_argument('v')    # URL上的参数 v： 访问时访问 http://127.0.0.1:8888/index?v= XXX
#         print('请求来了',value)
#
#         http = httpclient.AsyncHTTPClient()
#         # yield http.fetch('https://www.google.com.hk/',self.done)
#         # yield http.fetch('https://cn.bing.com/',self.done)
#         yield http.fetch("https://www.baidu.com/",self.done)  # Future对象
#
#     def done(self,response):
#         print('获取结果:',response)
#         self.write('完成')
#         self.finish()
#
# def make_app():
#     return tornado.web.Application([
#         (r"/index", index_Handler),
#     ], )
#
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)  # 监听端口
#     tornado.ioloop.IOLoop.current().start()

'''示例:异步非阻塞2 != 获取结果'''
# from tornado.concurrent import Future
# from tornado import gen
#
#
# class index_Handler(tornado.web.RequestHandler):
#
#     @gen.coroutine
#     def get(self):
#         value = self.get_query_argument('v')  # URL上的参数 v： 访问时访问 http://127.0.0.1:8888/index?v= XXX
#         print('请求来了', value)
#
#         f = Future()
#         f.add_done_callback(self.done)
#         yield f   Future对象
#
#     def done(self, response):
#         print('获取结果:', response)
#         self.write('完成')
#         self.finish()
#
#
# def make_app():
#     return tornado.web.Application([
#         (r"/index", index_Handler),
#     ], )
#
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)  # 监听端口
#     tornado.ioloop.IOLoop.current().start()

'''示例:异步非阻塞2 + 断开连接 = 获取结果2'''
# from tornado.concurrent import Future
# from tornado import gen
#
# FU_LIST = []
# class index_Handler(tornado.web.RequestHandler):
#
#     @gen.coroutine
#     def get(self):
#         value = self.get_query_argument('v')  # URL上的参数 v： 访问时访问 http://127.0.0.1:8888/index?v= XXX
#         print('请求来了', value)
#
#         f = Future()
#         f.add_done_callback(self.done)
#         FU_LIST.append(f)
#         yield f   Future对象
#
#     def done(self, response):
#         print('获取结果:', response)
#         self.write('完成')
#         self.finish()
#
# class Stop_Handler(tornado.web.RequestHandler):
#     def get(self):
#         f = FU_LIST.pop()
#         f.set_result('666')
#         self.write('终止一个')
#
#
#
# def make_app():
#     return tornado.web.Application([
#         (r"/index", index_Handler),
#         (r"/stop", Stop_Handler),
#     ], )
#
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)  # 监听端口
#     tornado.ioloop.IOLoop.current().start()

