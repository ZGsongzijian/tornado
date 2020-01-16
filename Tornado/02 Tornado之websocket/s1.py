import tornado.ioloop
import tornado.web
from tornado.websocket import WebSocketHandler

'''示例: websocket'''
class index_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class websocket_Handler(WebSocketHandler):
    def open(self, *args: str, **kwargs: str):
        print('有客户端给我发送 websocket请求')

    def on_message(self, message):
        # 服务器接收消息
        print('有客户端发送消息,内容是:',message)

        # 向客户端发送消息
        self.write_message('服务端发送过来的消息' + message )

    def on_close(self):
        print('这个websocket客户端要断开连接了')


def make_app():
    return tornado.web.Application([
        (r"/index", index_Handler),
        (r"/msg", websocket_Handler),
    ], )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # 监听端口
    tornado.ioloop.IOLoop.current().start()

'''浏览器控制台'''
# 查看是否连接ws    ws
# 向浏览器发送消息  ws.send(666)
# 重新连接ws       ws = new WebSocket('ws://127.0.0.1:8888/msg')
# 断开连接         ws.close()