# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:28:43 2020

@author: Administrator
"""

def get_min_max(ints):
     """
     Return a tuple(min, max) out of list of unsorted integers.

     Args:
       ints(list): list of integers containing one or more integers
     """
     assert len(ints) >0, "Enter correct integer list!"
     maxnum = float('inf')
     minnum = -float('inf')
     for n in ints:
         if n < maxnum:
             maxnum = n
         if n > minnum:
             minnum = n
     return (maxnum,minnum)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")