
"""
How it works (quick intuition)
1) Start from the second element
2) Compare it with elements before it
3) Shift larger elements to the right
4) Insert the element at its correct position

Key Characteristics

✔ Simple & Intuitive
✔ In-place Sorting
✔ Stable Algorithm
❌ Slow for large data
❌ Performance-critical systems

"""

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]      # current element
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Example usage:
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90, 5]
    sorted_array = insertion_sort(sample_array)
    print("Sorted array is:", sorted_array)