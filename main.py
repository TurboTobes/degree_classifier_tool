#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:13:32 2020

@author: user
"""

from modules.lvl6_average_calculator import lvl6_req
from modules.Degree_classification_calculator import deg_class

print("""
Welcome to the KU degree classification calculator. Here you can calculate what your final classification will be, or you can calculate what you need to get in level 6 to meet your target.
Which would you like to do?
\t1) calculate your classification (enter '1')
\t2) calculate what you need for your targetted classification (enter '2')      
""")

choice = input()
choice = int(choice)
if choice == 1:
    deg_class()
else:
    lvl6_req()
