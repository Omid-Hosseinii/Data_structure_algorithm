def heapify(arr, size_arr, index_current_root):

    largest = index_current_root
    left = 2 * index_current_root + 1
    right = 2 * index_current_root + 2

    if left < size_arr and arr[left] > arr[largest]:
        largest = left

    if right < size_arr and arr[right] > arr[largest]:
        largest = right

    if largest != index_current_root:
        arr[index_current_root], arr[largest] = arr[largest], arr[index_current_root] # swap
        heapify(arr, size_arr, largest)


def heap_sort(array):
    size_arr = len(array)

    # for heapify
    for i in range(size_arr // 2 - 1, -1, -1):
        heapify(array, size_arr, i)

    # for change the largest item (which is main root) with last node.
    for i in range(size_arr - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


example_array = [4, 10, 3, 5, 1]

print("original array:\t", example_array)
heap_sort(example_array)
print("heap sort array:\t", example_array)
