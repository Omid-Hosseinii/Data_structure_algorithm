"""
    Merge sort algorithm:
            We use recursive concept to sort unsorted array.

       Time Complexity:
            Best Case: O(n log n)
            Average Case: O(n log n)
            Worst Case: O(n log n)

       Space Complexity:
            the Space complexity is O(n), because we need extra list during merge 2 sorted list.
"""


sample_sorted_list1 = [1, 2, 4, 5, 8, 10]
sample_sorted_list2 = [4, 8, 12]

sample_unsorted_list = [3, 5, 1, 9, 7, 22, 16]


def merge_sorted_list(list1, list2):
    """
        Sort 2 sorted array.
    """
    list_ = []
    len1 = len(list1)
    len2 = len(list2)

    # counter for iterate both list
    i = j = 0

    while i < len1 and j < len2:
        if list1[i] < list2[j]:
            list_.append(list1[i])
            i += 1
        else:
            list_.append(list2[j])
            j += 1

    return list_ + list1[i:] + list2[j:]


def merge_sort(arr):
    """
        merge sort algorithm.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_list = arr[:mid]
    right_right = arr[mid:]

    individual_left_list = merge_sort(left_list)
    individual_right_list = merge_sort(right_right)

    return merge_sorted_list(individual_left_list, individual_right_list)


if __name__ == '__main__':

    print("Merge function test:")
    print("sorted list1 is:\t", sample_sorted_list1)
    print("sorted list2 is:\t", sample_sorted_list2)
    print("merge two sorted list:\t", merge_sorted_list(sample_sorted_list1, sample_sorted_list2))
    print(100*"-")

    print("unsorted list:\t", sample_unsorted_list)
    print("Sorted array using merge sort algorithm:\t", merge_sort(sample_unsorted_list))
