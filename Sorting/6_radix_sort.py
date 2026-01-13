def radix_sort(arr):
    max_num = max(arr)
    exp = 1 # Exponent representing the current digit place

    while max_num // exp > 0:
        print(arr, "\n")
        counting_sort(arr, exp)
        exp *= 10


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[] 
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    print("1 count", count, "\n")
    # Change count[i] so that it now contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    print("2 count", count, "\n")
    
    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]


# Example usage
my_array = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(my_array)
print("Sorted array:", my_array)