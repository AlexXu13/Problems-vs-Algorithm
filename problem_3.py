# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:57:18 2020

@author: Zixia xu
"""


def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        mid_value = alist[0]
        low = [i for i in alist[1:] if i <= mid_value]
        high = [i for i in alist[1:] if i > mid_value]
        return quick_sort(high) + [mid_value] + quick_sort(low)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    assert isinstance(input_list, list), "Enter a correct list!"
    length = len(input_list)
    assert length > 0, "Enter a correct list!"
    input_list = quick_sort(input_list)
    left = ''
    right = ''
    flag = 0
    for num in input_list:
        if flag % 2 == 0:
            left += str(num)
            flag += 1
        else:
            right += str(num)
            flag += 1
    return [int(left), int(right)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
