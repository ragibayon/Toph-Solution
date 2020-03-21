# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:53:15 2020
2
hello world
@author: Ragib Shahariar Ayon
"""
n=int(input())
input_string=input()

list1=input_string.split(' ')
list2=[]
for item in list1:
    list2.append(" ")
    for ch in item:
        list2.append(chr(ord(ch)-n))
    
output_string=''.join(list2)
print(output_string.strip())