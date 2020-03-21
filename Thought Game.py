# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:37:14 2020

@author: Ragib Shahariar Ayon
"""

input_time=int(input())

for i in range(input_time):
    s=input()
    a,b=s.split()
    avg=(int(a)+int(b))//2
    if avg%2==0:
        print("Sadia will be happy.")
    else:
        print("Oops!")
    