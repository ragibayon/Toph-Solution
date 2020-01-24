# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:10:56 2020

@author: hp
"""

f=int(input())
a=input()
input_list=a.split()

n=len(input_list)
test_list=[None]*n

for i in range(0, len(input_list)):
    test_list[i]=int(input_list[i])
test_list.sort()
print(test_list[f-1])

