#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:45:38 2020
РАШН ЭДИШН
@author: mbtor
"""
import math

def binary_search(lst):
    low = 0 
    high = len(lst) - 1
    print("Ну, погнали")
    while  low <= high:
        mid = int((low + high) / 2)
        choice = input(" %d Это число, верно?\n" %lst[mid])
        if choice == 'yes':
            print(")))))")
            break
        elif choice == '<':
            high = lst[mid] - 1
        elif choice == '>':
            low = lst[mid] + 1
        else:
            print("Какого черта, бро?")

maximum = int(input("Ку, я могу отгадать любое, загаданное тобою число от нуля до какого-то максимального значения, выбери это максимальное значение\n"))
lst = range(0, maximum + 1)
steps = math.log(maximum, 2) 
print ("Изи, сделаю это не более чем за %d попыток\n" %steps)
s = "Короче, если я угадаю, напиши мне \"yes\", если твое число меньше чем то, что я написал, то \"<\", если твое число больше чем я написал, то \">\". Ты понял? Скажи \"да\" если понял"
print(s)
choice = input()
while choice != 'да':
    print("Серьезно?\n")
    print(s)
    choice = input() 
binary_search(lst)