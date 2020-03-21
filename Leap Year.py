# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:56:14 2020
Leap Years
@author: Ragib Shahariar Ayon
"""

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return 'Yes'
            return 'No'
        return 'Yes'
    else:
        return 'No'
    
print(leap_year(int(input())))


