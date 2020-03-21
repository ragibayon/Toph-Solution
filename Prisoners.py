# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:25:40 2020
3
1
10
3
1 2 3
9
200 933 100 6 20 103 310 1 143
@author: Ragib Shahariar Ayon
"""


def bounty_count(prisoner_bounty=0,prisonar_count=0):
    bounty_sum=0
    for bounty in prisoner_bounty:
        bounty_sum+=int(bounty)
        total_bounty=(1/prisonar_count)*bounty_sum
    return total_bounty
    


test_case=int(input())

for i in range(test_case):
    prisonar_count=int(input())
    prisoner_bounty=input().split()
    print(bounty_count(prisoner_bounty,prisonar_count))

