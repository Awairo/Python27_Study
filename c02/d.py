#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dict
d = {'Micheel': 95, 'Bob': 75, 'Tracy': 85}
print d['Micheel']
print 'xu' in d
print d.get('xu', -1)
d.pop('Bob')
print d


#set 
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s = set([1, 2, 3])
print s
s = set([1, 1, 2, 2, 3, 3])
print s