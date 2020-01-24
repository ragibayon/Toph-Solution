# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:01:28 2020

@author: Ragib Shahariar Ayon
"""
"""
convert to string
remove 1st two index
replace 0 with None
int(string,2)
"""


a=int(input())
b=str(bin(a))
c=b[2:]
d=c.replace("0","")
e=int(d,2)
print(e)

