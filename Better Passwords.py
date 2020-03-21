# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:35:21 2020
Better Passwords
@author: Ragib Shahariar Ayon
"""
#s='unsophisticated'
s=input()
replace_dict={
    "s":"$",
    "i":"!",
    "o":"()"
    }
input_list=list(s)
i=0
for index,ch in enumerate(input_list):
    for key in replace_dict.keys():
        if ch not in list(replace_dict.keys()):
            continue
        else:
            
            input_list[index]=replace_dict[ch]


input_list[0]=input_list[0].upper()
input_list.append('.')

output=''.join(map(str, input_list))
print(output)
