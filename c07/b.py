#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student('XuXu', 40)
s.score = 70
print(s.score)