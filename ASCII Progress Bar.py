# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:24:30 2020
ASCII Progress Bar
62.3
[++++++....] 62%

0.0 ≤ P ≤ 100.0
@author: Ragib Shahariar Ayon
"""

input_string_int=int(float(input()))

n=input_string_int//10

plus_sign='+'*n
dot_sign='.'*(10-n)
percent=input_string_int


print('[{}{}] {}%'.format(plus_sign,dot_sign,percent))

