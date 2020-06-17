# -*- coding: utf-8 -*-

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #assert number>=0, "Number should be more than zero!"
    if number==None or number < 0:
        return None
    if number==0:
        return number
    if number==1 or number==2 or number==3:
        return 1
    left = 1
    right = number
    while left+1 < right:
        mid = (right + left)//2
        if mid * mid < number:
           left = mid
        elif mid * mid > number:
            right = mid
        else:
            return mid
    return left


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (None == sqrt(None)) else "Fail")