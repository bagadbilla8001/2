def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] to store actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy output to arr
    for i in range(n):
        arr[i] = output[i]

    print(f"After sorting with exp={exp}: {arr}")


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Input array
arr= list(map(int,input("Enter the unsorted array-").split()))

print("Original Array:", arr)

# Sort the array using Radix Sort
radix_sort(arr)

print("Sorted Array:", arr)
