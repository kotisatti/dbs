# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:03:01 2020

@author: Koteswararao Sathi
"""


#Question 2

def Get_Pairs(lst, k):
    res = []
    lst.sort()
    for e in lst:
        if e + k in lst and k < 0:
            res.append(tuple((e + k, e)))
        elif e + k in lst and k >0:
            res.append(tuple((e , e + k)))
        else:
            pass
    return res


            


