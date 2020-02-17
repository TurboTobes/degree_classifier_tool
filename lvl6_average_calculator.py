#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:47:37 2020

@author: user
"""
def lvl6_req():
    level5_list = []

    for i in range (0,4):
        value = input(f"Please enter your level 5 module {i+1} grade (as a percentage):\n")
        value= int(value)
        level5_list.append(value)



    level5_list.sort()


    level5_average = ((level5_list[0]/2)+level5_list[1]+level5_list[2]+level5_list[3])/3.5
    print(f"\nYour average for level 5 is: {round(level5_average)}%. This is 20% of your classification.")

    req_first = (350-level5_average)/4
    req_two_one = (300-level5_average)/4
    req_two_two = (250-level5_average)/4
    req_third = (200-level5_average)/4

    print(f"""
          To get a 1st, you will need to average {round(req_first)}% in level 6.\n
          To get a 2:1, you will need to average {round(req_two_one)}% in level 6.\n      
          To get a 2:2, you will need to average {round(req_two_two)}% in level 6.\n
          To get a 3rd, you will need to average {round(req_third)}% in level 6.\n
          Please bear in mind that the averages used in each level drop half of your lowest scoring module, so the actual average you need may be slightly lower than predicted above.\n
          """)