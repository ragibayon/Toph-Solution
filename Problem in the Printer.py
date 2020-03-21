# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:01:36 2020

@author: Ragib Shahariar Ayon
"""


#input_s=input()
#input_s="once a bee flied. then it died.but its soul is alive. the end."
input_s='0nce a 6ee f1ied. then it died.6ut it5 50u1 i5 a1ive. the end.'
s=input_s.replace('the end.','')




numbers_dict={"b":"6",
              "6":"b",
              "g":"9",
              "9":"g",
              "l":"1",
              "1":"l",
              "o":"0",
              "0":"o",
              "s":"5",
              "5":"s",
              "z":"2",
              "2":"z",}

lst=list(s)

for index,char in enumerate(lst):
    if char not in list(numbers_dict.keys()):
        continue    
    else:
        lst[index]=numbers_dict[char]

out=''.join(map(str,lst))
print(out)
