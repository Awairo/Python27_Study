#!/usr/bin/env python
# -*- coding: utf-8 -*-

classmates = ['Micheal', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[-1]

classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates
classmates.pop()
print classmates
classmates.pop(1)
print classmates
classmates[1] = 'Xu'
print classmates

L = ['Apple', 123, True]

s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)

#Tuple  tuple一旦初始化就不能修改
# tuple的每个元素，指向永远不变

classmates = ('Micheal', 'Bob', 'Tracy')

#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

