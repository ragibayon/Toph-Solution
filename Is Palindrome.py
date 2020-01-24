# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 03:16:47 2020

@author: hp
"""

# a=list(input())
a = "eye"
b = a[::-1]  # reverses a list
c = ",".join(b)  # seperator.join(type)
d = c.replace(",", "")  # from.replace("this","to this")
if a == d:
    print("Yes")
else:
    print("No")
