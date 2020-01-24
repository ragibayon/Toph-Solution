# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:10:37 2020

@author: hp
"""

a=int(input())
count=0

for i in range (2, a):
    c=a%i
    if c==0:
        count=count+1
if count==0:
    print("Yes")        
else:
    print("No")    