def rotated_array_search(input_list, number, mid=0):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not isinstance(input_list,list):
        return -1
    length = len(input_list)
    if length == 0:
        return -1
    start = 0
    end = len(input_list)
    while start <= end:
        mid = (start+end) // 2
        #print('p', mid)
        if mid == length-1 or input_list[0] < input_list[-1]  :
            mid = 0
            break
        if input_list[mid] < input_list[mid-1]:
            break
        if input_list[mid] > input_list[0]:
            start = mid
        else:
            end = mid

    if input_list[mid] <= number and input_list[-1] >= number:
        start = mid
        end = length
    else:
        start = 0
        end = mid

    while start <= end:
        mid = (start+end) // 2
        if input_list[mid] < number :
            start = mid+1
        elif input_list[mid] > number:
            end = mid-1
        else:
            return mid
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([{6,7,89}, 10])
