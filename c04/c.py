#!/usr/bin/env python
# -*- coding: utf-8 -*-

L = []
for x in range(1, 11):
    L.append(x * x)
print L

print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]

print [m + n for m in 'ABC' for n in 'XYZ']

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]