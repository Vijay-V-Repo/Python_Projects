# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:37:45 2020

@author: VIJAY
"""

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3:"))
if num1>num2 :
    if num1>num3:
        print("Max. of the three numbers is :",num1)
    else :
        print("max is ",num3)
else :
    if num2>num3 :
        print("max is :",num2)
    else:
        print("Max is :",num3)
        
    