"""
    [23, 1, 10, 5, 2]

"""

eg_arr = [23, 1, 10, 5, 2, 80]


def insertion_sort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(arr)


insertion_sort(eg_arr)
