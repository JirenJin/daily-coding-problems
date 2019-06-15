"""
Problem Definition:
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""

# this is a wrong solution
# conflict test case: [6, 6, 6, 2, 3, 3, 4, 5, 6, 7]
def can_become_sorted(array):
    first_unsorted = -1
    for i in range(len(array) - 1):
        if array[i+1] < array[i]:
            first_unsorted = i + 1
            break
    if first_unsorted == -1:
        return True
    second_unsorted = len(array)
    for i in range(len(array) - 1, 0, -1):
        if array[i-1] > array[i]:
            second_unsorted = i - 1
            break
    return first_unsorted - second_unsorted == 1


# my solution
def can_become_sorted(array):
    count = 0
    for i in range(len(array) - 1):
        if array[i+1] < array[i]:
            count += 1
            if count == 2:
                return False
            # edge case: when array[i-1] and array[i+1] are inside the range (array[i+1], array[i])
            if i > 0 and i + 2 < len(array) and array[i-1] > array[i+1] and array[i+2] < array[i]:
                return False
    return True


# sample solution
def check(lst):
    count = 0
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            if count > 0:
                return False
            if i - 1 >= 0 and i + 2 < len(lst) and lst[i] > lst[i + 2] and lst[i + 1] < lst[i - 1]:
                return False
            count += 1
    return True


if __name__ == "__main__":
    import random
    test_cases = []
    for _ in range(10000):
        test_cases.append([random.randint(1, 7) for _ in range(7)])
#     test_cases = [
        # [10, 5, 7],
        # [10, 5, 1],
        # [1,2,3,8,5,6],
        # [1,2,3,2,5,6],
        # [1,2,3,2,2,5,6],
        # [1,2,3,2,1,5,6]

#     ]
    # truths = [True, False, True, True, True, False]
    for test_case in test_cases:
        if can_become_sorted(test_case) != check(test_case):
            print(test_case)
            print("Wrong")
            break
    else:
        print("Correct")



