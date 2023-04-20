#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python允许你同时为多个变量赋值

a = b = c = 1

print(a)
print(b)
print(c)

a, b, c = 1, 2, "john"

print(a)
print(b)
print(c)

# Python有五个标准的数据类型：
#
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）




# Python字符串

str = 'Hello World!'

print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第六个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串


# Python列表

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

# Python 元组

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第四个（不包含）的元素
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组



# 以下对元组的操作是无效的，因为元组不允许更新，而列表是允许更新的 ！！！！



# Python 字典

# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
#
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}


print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值


# Python数据类型转换

# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
#
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
#
# 函数	描述
# int(x [,base])
#
# 将x转换为一个整数
#
# long(x [,base] )
#
# 将x转换为一个长整数
#
# float(x)
#
# 将x转换到一个浮点数
#
# complex(real [,imag])
#
# 创建一个复数
#
# str(x)
#
# 将对象 x 转换为字符串
#
# repr(x)
#
# 将对象 x 转换为表达式字符串
#
# eval(str)
#
# 用来计算在字符串中的有效Python表达式,并返回一个对象
#
# tuple(s)
#
# 将序列 s 转换为一个元组
#
# list(s)
#
# 将序列 s 转换为一个列表
#
# set(s)
#
# 转换为可变集合
#
# dict(d)
#
# 创建一个字典。d 必须是一个序列 (key,value)元组。
#
# frozenset(s)
#
# 转换为不可变集合
#
# chr(x)
#
# 将一个整数转换为一个字符
#
# unichr(x)
#
# 将一个整数转换为Unicode字符
#
# ord(x)
#
# 将一个字符转换为它的整数值
#
# hex(x)
#
# 将一个整数转换为一个十六进制字符串
#
# oct(x)
#
# 将一个整数转换为一个八进制字符串