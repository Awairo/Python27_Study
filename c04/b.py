#!/usr/bin/env python
# -*- coding: utf-8 -*-


d = {'a':1, 'b':2, 'c':3}
for key in d:
    print key

for value in d.itervalues():
    print value

for k, v in d.iteritems():
    print(k, v)

from collections import Iterable
print isinstance('abc', Iterable) # str是否可迭代
print isinstance([1,2,3], Iterable) # list是否可迭代
print isinstance(123, Iterable) # 整数是否可迭代

for i, value in enumerate(['A', 'B', 'C']):
    print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y