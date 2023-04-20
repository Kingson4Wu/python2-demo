#!/usr/bin/python
# -*- coding: UTF-8 -*-

var1 = 'Hello World!'
var2 = "Python Runoob"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

# 字符串连接
var1 = 'Hello World!'

print "输出 :- ", var1[:6] + 'Runoob!'

# 字符串运算符
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。


a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
print "a[1] 输出结果：", a[1]
print "a[1:4] 输出结果：", a[1:4]

if "H" in a:
    print "H 在变量 a 中"
else:
    print "H 不在变量 a 中"

if "M" not in a:
    print "M 不在变量 a 中"
else:
    print "M 在变量 a 中"

print r'\n'
print R'\n'

# 字符串格式化

print "My name is %s and weight is %d kg!" % ('Zara', 21)

# 字符串格式化符号

# Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。 !!!!!


# 三引号


# Unicode 字符串
# Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单：

print(u'Hello World !')

print(u'Hello\u0020World !')

# 字符串内建函数 !!


