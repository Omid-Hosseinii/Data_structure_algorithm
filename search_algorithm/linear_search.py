"""
    Linear Search:
        Iterate over all the elements of the array and check if it the current element is equal to the target element.

    Time complexity:
        Best case: O(1)
        Worst case and Average case: O(n)
    Space complexity: O(1)
"""

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return item
    return "The given element is not present in the array."


sample_list = [1, 2, 3, 50, 3, 9, 12, 13, 15, 20, 30]

print(linear_search(sample_list, 51))
