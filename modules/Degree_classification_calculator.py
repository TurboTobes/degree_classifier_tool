#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:12:35 2020

@author: user
"""
def deg_class():
    level5_list = []
    level6_list = []

    for i in range (0,4):
        value = input(f"Please enter your level 5 module {i+1} grade (as a percentage):\n")
        value= int(value)
        level5_list.append(value)

    for i in range (0,4):
        value = input(f"Please enter your level 6 predicted module {i+1} grade (as a percentage):\n")
        value= int(value)
        level6_list.append(value)

    level5_list.sort()
    level6_list.sort()

    level5_average = ((level5_list[0]/2)+level5_list[1]+level5_list[2]+level5_list[3])/3.5
    print(f"\nYour average for level 5 is: {round(level5_average)}%. This is 20% of your classification.")
    level6_average = ((level6_list[0]/2)+level6_list[1]+level6_list[2]+level6_list[3])/3.5
    print(f"Your average for level 6 is: {round(level6_average)}%. This is 80% of your classification.")
    
    degree_class = ((level5_average * 20)+(level6_average * 80))/100
    
    if degree_class >= 70:
        print(f"You overall grade is: {round(degree_class)}%, which means you got a 1st!")
    elif degree_class < 70 and degree_class >= 60:
        print(f"You overall grade is: {round(degree_class)}%, which means you got a 2:1!")
    elif degree_class < 60 and degree_class >= 50:
        print(f"You overall grade is: {round(degree_class)}%, which means you got a 2:2!")
    elif degree_class < 50 and degree_class >= 40:
        print(f"You overall grade is: {round(degree_class)}%, which means you got a 3rd!")
    else:
        print(f"Your overall grade is: {round(degree_class)}%, which means you didn't classify.")