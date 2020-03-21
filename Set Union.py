# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:12:37 2020
Set Union
@author: Ragib Shahariar Ayon
"""

set_count=input()
set1=set(input().split())
set2=set(input().split())

set3=set1|set2
print(' '.join(map(str,sorted(set3))))