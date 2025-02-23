"""
    bubble sort algorithm:

        Time complexity:
            Average Case = O(n)
            Worst Case = O(n * n)
"""

from random import randint

_list_test = [randint(1, 10) for i in range(5)]

def bubble_sort(arr):
    len_ = len(arr)
    swapped_flag = False
    for i in range(len_ - 1):
        for j in range(len_ - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped_flag = True

        if not swapped_flag:
            break


    print("Sorted array with bubble sort:\t", arr)

print("Unsorted list:\t", _list_test)
bubble_sort(_list_test)
