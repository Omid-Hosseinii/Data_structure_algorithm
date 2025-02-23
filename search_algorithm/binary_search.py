"""
    Binary Search
    Time and Space Complexity:
        Time complexity: O(log n)
        Space complexity: O(1)

    We can implement Binary Search Algorithm in 2 ways:
    - Iterative Binary Search Algorithm
    - Recursive Binary Search Algorithm
"""

sample_list = [1, 5, 9, 12, 18, 25, 50, 77, 78, 79, 99, 150]

def binary_search_iterative(arr, element):
    low_index = 0
    high_index = len(arr) - 1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2

        if arr[mid_index] == element:
            return mid_index

        elif arr[mid_index] < element:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1

    return "Not Found"


def binary_search_recursive(arr, element):
    low_index = 0
    high_index = len(arr) - 1

    if low_index > high_index:
        return "Not Found"

    middle_index = (low_index + high_index) // 2



    if arr[middle_index] == element:
        return middle_index

    elif arr[middle_index] > element:
        return binary_search_recursive(arr[:middle_index], element)

    else:
        return binary_search_recursive(arr[middle_index:], element)

    # return "Not Found"


if __name__ == '__main__':

    print("Test Iterative Binary Search Algorithm:")
    print("Found the index of element =>\t",
          binary_search_iterative(sample_list, 9))


    print()

    print("Test Recursive Binary Search Algorithm:")
    print("Found the index of element =>\t",
          binary_search_recursive(sample_list, 9))
