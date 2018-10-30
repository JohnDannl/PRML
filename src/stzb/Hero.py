#!/usr/bin/env python
#-*- coding:UTF-8 -*-
'''
Created on 2018��10��30��

@author: JohnDannl
'''
class Hero(object):
    def __init__(self, name, star, level, corps):
        self.name = name
        self.star = star
        self.level = level
        self.corps = corps

if __name__ == '__main__':
    MaChao = Hero("MaChao", 4, 10, "")
    print(MaChao.name, ":", MaChao.level)