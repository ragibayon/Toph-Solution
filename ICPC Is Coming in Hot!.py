# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:29:32 2020

@author: Ragib Shahariar Ayon
"""
s='1213'
lst=[]
for charecter in s:
    lst.append(charecter)
print(max(lst ,key=lst.count))

print(lst.count('1'))