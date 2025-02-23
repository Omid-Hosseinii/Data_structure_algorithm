"""
   Quick sort algorithm.

   Time complexity:
        Best case: O(n log n)
        Worst case: O(n * n)
        Average case: o(n log n)

   Space complexity:
        O(n): using list comprehension approach.
        o(1): using in-place swapped.
"""

unsorted_list_example = [3, 4, 5, 9, 1, 2]

less = [1, 2]
middle = [3]
greater = [4, 5, 9]


def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list[0]
        greater_than_pivot = [item for item in unsorted_list[1:] if item >= pivot]
        less_than_pivot = [item for item in unsorted_list[1:] if item < pivot]

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



if __name__ == '__main__':

    print(less + middle + greater)
    print("unsorted list is: ", unsorted_list_example, "\n")

    print("sorted list is: ", quick_sort(unsorted_list_example))
