"""

How Selection Sort Works

Assume the first element is the smallest
Find the smallest element in the unsorted part
Swap it with the first unsorted position
Move the boundary of sorted part by one

Key Characteristics

✔ Simple to understand
✔ Works well for small datasets
❌ Slow for large data
❌ Not stable (relative order may change)

"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find the index of the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example usage
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
print("Sorted array:", selection_sort(my_array))