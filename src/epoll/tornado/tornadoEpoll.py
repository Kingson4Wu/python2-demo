import errno
import functools
import tornado.ioloop
import socket

'''
http://www.jianshu.com/p/0fb633010296
'''
def handle_connection(connection, address):
    """ 处理请求，返回数据给客户端 """
    data = connection.recv(2014)
    print data
    connection.send(data)


def connection_ready(sock, fd, events):
    """ 事件回调函数，主要用于socket可读事件，用于获取socket的链接 """
    while True:
        try:
            connection, address = sock.accept()
        except socket.error as e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        connection.setblocking(0)
        handle_connection(connection, address)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(("", 5000))
    sock.listen(128)
    # 使用tornado封装好的epoll接口，即IOLoop对象
    io_loop = tornado.ioloop.IOLoop.current()
    callback = functools.partial(connection_ready, sock)
    # io_loop对象注册网络io文件描述符和回调函数与io事件的绑定
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
    io_loop.start()