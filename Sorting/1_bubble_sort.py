"""
Bubble Sort Implementation

How Bubble Sort Works (Intuition)
------------------------------------
Compare adjacent elements
Swap if they are in the wrong order
After each pass, the largest element “bubbles” to the end

🔹 Key Characteristics of Bubble Sort
---------------------------------------
✔ Very simple
✔ Stable
✔ In-place
❌ Very slow for large datasets
❌ Mostly used for learning

"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:   # optimization to stop if the array is already sorted
            break

    return arr


# Example
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
print("Sorted array:", bubble_sort(my_array))