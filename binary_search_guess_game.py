#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:45:38 2020

@author: mbtor
"""
import math

def binary_search(lst):
    low = 0
    high = len(lst) - 1
    print("okay, let's do this, man")
    while  low <= high:
        mid = int((low + high) / 2)
        choice = input(" %d is that the number you made?\n" %lst[mid])
        if choice == 'yes':
            print(")))))")
            break
        elif choice == '<':
            high = lst[mid] - 1
        elif choice == '>':
            low = lst[mid] + 1
        else:
            print("dafaq bro?")

maximum = int(input("Hi, i can guess the numba you have made, let's tryin. The floor numb is 0 , what is the highest numb?\n"))
lst = range(0, maximum + 1)
steps = math.log(maximum, 2) 
print ("Ah, easy, i can solve it not more than %d iterations\n" %steps)
s = "If i guess you numb type me \"yes\", if your numb less than mine type me \"<\", if your numb more than mine type me \">\". Get it?"
print(s)
choice = input()
while choice != 'yes':
    print("dafaq bro?\n")
    print(s)
    choice = input() 
binary_search(lst)