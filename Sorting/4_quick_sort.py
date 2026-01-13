"""
Quick sort

How Quick Sort Works
1) Choose a pivot element
2) Partition the array into:
   Elements less than pivot
   Elements equal to pivot
   Elements greater than pivot
3) Recursively apply the same steps to left and right parts


Key Characteristics of Quick Sort

✔ Very fast in practice
✔ Divide-and-conquer algorithm
✔ In-place version possible
❌ Not stable
❌ Worst case occurs with bad pivot choice

"""

def partition(arr, low, high):
    pivot = arr[high]
    print(low, high,"Pivot:", pivot)
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


# Example
my_array = [20, 2, 7, 12, 15, 1, 6, 8]
quick_sort_inplace(my_array, 0, len(my_array) - 1)
print("Sorted array:", my_array)
