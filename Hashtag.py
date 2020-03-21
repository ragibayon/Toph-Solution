# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:31:51 2020

@author: Ragib Shahariar Ayon
"""


#input_str='ayon'
input_str=input()
if input_str.find('#') == 0:
    spc_replaced_str=input_str.replace(' ','')    
    print(spc_replaced_str)
else:
    print(input_str)

