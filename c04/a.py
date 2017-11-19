#!/usr/bin/env python
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print L[0:3]
print L[:3]
print L[1:3]
print L[-2:]
print L[-2:-1]

L = range(100)
print L[:10:2]  #前10个数，每两个取一个
print L[::5]    #所有数，每5个取一个
print L[:]      #复制

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
#字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串