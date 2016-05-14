多路复用I/O
在简明网络I/O模型文章可以知道常用的IO模型。其中同步模型中，使用多路复用I/O可以提高服务器的性能。

在多路复用的模型中，比较常用的有select模型和poll模型。这两个都是系统接口，由操作系统提供。当然，Python的select模块进行了更高级的封装。select与poll的底层原理都差不多。下面就介绍select。

select 原理
网络通信被Unix系统抽象为文件的读写，通常是一个设备，由设备驱动程序提供，驱动可以知道自身的数据是否可用。支持阻塞操作的设备驱动通常会实现一组自身的等待队列，如读/写等待队列用于支持上层(用户层)所需的block或non-block操作。设备的文件的资源如果可用（可读或者可写）则会通知进程，反之则会让进程睡眠，等到数据到来可用的时候，再唤醒进程。

这些设备的文件描述符被放在一个数组中，然后select调用的时候遍历这个数组，如果对于的文件描述符可读则会返回改文件描述符。当遍历结束之后，如果仍然没有一个可用设备文件描述符，select让用户进程则会睡眠，直到等待资源可用的时候在唤醒，遍历之前那个监视的数组。每次遍历都是线性的。

select 回显服务器
select涉及系统调用和操作系统相关的知识，因此单从字面上理解其原理还是比较乏味。用代码来演示最好不过了。使用python的select模块很容易写出下面一个回显服务器：

import select
import socket
import sys

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

inputs = [server, sys.stdin]
running = True

while True:
    try:
        # 调用 select 函数，阻塞等待
        readable, writeable, exceptional = select.select(inputs, [], [])
    except select.error, e:
        break

    # 数据抵达，循环
    for sock in readable:
        # 建立连接
        if sock == server:
            conn, addr = server.accept()
            # select 监听的socket
            inputs.append(conn)
        elif sock == sys.stdin:
            junk = sys.stdin.readlines()
            running = False
        else:
            try:
                # 读取客户端连接发送的数据
                data = sock.recv(BUFFER_SIZE)
                if data:
                    sock.send(data)
                    if data.endswith('\r\n\r\n'):
                        # 移除select监听的socket
                        inputs.remove(sock)
                        sock.close()
                else:
                    # 移除select监听的socket
                    inputs.remove(sock)
                    sock.close()
            except socket.error, e:
                inputs.remove(sock)

server.close()
运行上述代码，使用curl访问http://localhost:5000，即可看命令行返回请求的HTTP request信息。

下面详细解析上述代码的原理。

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
上述代码使用socket初始化一个TCP套接字，并绑定主机地址和端口，然后设置服务器监听。

inputs = [server, sys.stdin]
这里定义了一个需要select监听的列表，列表里面是需要监听的对象（等于系统监听的文件描述符）。这里监听socket套接字和用户的输入。

然后代码进行一个服务器无线循环。

try:
    # 调用 select 函数，阻塞等待
    readable, writeable, exceptional = select.select(inputs, [], [])
except select.error, e:
    break
调用了select函数，开始循环遍历监听传入的列表inputs。如果没有curl服务器，此时没有建立tcp客户端连接，因此改列表内的对象都是数据资源不可用。因此select阻塞不返回。

客户端输入curl http://localhost:5000之后，一个套接字通信开始，此时input中的第一个对象server由不可用变成可用。因此select函数调用返回，此时的readable有一个套接字对象（文件描述符可读）。

for sock in readable:
    # 建立连接
    if sock == server:
        conn, addr = server.accept()
        # select 监听的socket
        inputs.append(conn)
select返回之后，接下来遍历可读的文件对象，此时的可读中只有一个套接字连接，调用套接字的accept()方法建立TCP三次握手的连接，然后把该连接对象追加到inputs监视列表中，表示我们要监视该连接是否有数据IO操作。

由于此时readable只有一个可用的对象，因此遍历结束。再回到主循环，再次调用select，此时调用的时候，不仅会遍历监视是否有新的连接需要建立，还是监视刚才追加的连接。如果curl的数据到了，select再返回到readable，此时在进行for循环。如果没有新的套接字，将会执行下面的代码：

try:
    # 读取客户端连接发送的数据
    data = sock.recv(BUFFER_SIZE)
    if data:
        sock.send(data)
        if data.endswith('\r\n\r\n'):
            # 移除select监听的socket
            inputs.remove(sock)
            sock.close()
    else:
        # 移除select监听的socket
        inputs.remove(sock)
        sock.close()
except socket.error, e:
    inputs.remove(sock)
通过套接字连接调用recv函数，获取客户端发送的数据，当数据传输完毕，再把监视的inputs列表中除去该连接。然后关闭连接。

整个网络交互过程就是如此，当然这里如果用户在命令行中输入中断，inputs列表中监视的sys.stdin也会让select返回，最后也会执行下面的代码：

elif sock == sys.stdin:
    junk = sys.stdin.readlines()
    running = False
有人可能有疑问，在程序处理sock连接的是时候，假设又输入了curl对服务器请求，将会怎么办？此时毫无疑问，inputs里面的server套接字会变成可用。等现在的for循环处理完毕，此时select调用就会返回server。如果inputs里面还有上一个过程的conn连接，那么也会循环遍历inputs的时候，再一次针对新的套接字accept到inputs列表进行监视，然后继续循环处理之前的conn连接。如此有条不紊的进行，直到for循环结束，进入主循环调用select。

任何时候，inputs监听的对象有数据，下一次调用select的时候，就会繁返回readable，只要返回，就会对readable进行for循环，直到for循环结束在进行下一次select。

主要注意，套接字建立连接是一次IO，连接的数据抵达也是一次IO。

select的不足
尽管select用起来挺爽，跨平台的特性。但是select还是存在一些问题。
select需要遍历监视的文件描述符，并且这个描述符的数组还有最大的限制。随着文件描述符数量的增长，用户态和内核的地址空间的复制所引发的开销也会线性增长。即使监视的文件描述符长时间不活跃了，select还是会线性扫描。

为了解决这些问题，操作系统又提供了poll方案，但是poll的模型和select大致相当，只是改变了一些限制。目前Linux最先进的方式是epoll模型。

许多高性能的软件如nginx, nodejs都是基于epoll进行的异步。


