# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:17:39 2020

@author: hp
"""

n=int(input())
a=1
b=1

for i in range (0,n-2):# duita kom as 1,b khaya dise
    temp=a+b
    b=a
    a=temp
print(temp)