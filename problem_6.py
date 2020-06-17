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
     if len(ints)<=0:
         return "Enter correct integer list!"
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
#test case 1
l1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l1)
print ("Pass" if ((0, 9) == get_min_max(l1)) else "Fail")
#test case 2
l2 = [i for i in range(45, 501)]  # a list containing 45 - 500
random.shuffle(l2)
print ("Pass" if ((45, 500) == get_min_max(l2)) else "Fail")
#test case 3
l3 = [-1,3,6,90,45,50]  # a list containing 45 - 500
random.shuffle(l3)
print ("Pass" if ((-1, 90) == get_min_max(l3)) else "Fail")
#test case 4
l4 = []  # a list containing 45 - 500
random.shuffle(l4)
print ("Pass" if ("Enter correct integer list!" == get_min_max(l4)) else "Fail")



