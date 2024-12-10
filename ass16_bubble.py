def bubble_sort(arr):
    n = len(arr)
    print("\nBubble Sort Steps:")
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"After iteration {i + 1}: {arr}")
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    print("\nShell Sort Steps:")
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        print(f"After gap {gap}: {arr}")
        gap //= 2
    return arr

# Input: First year percentages
percentages=list(map(int,input("Enter the unsorted array").split()))

print("Original Array:", percentages)

# Bubble Sort
bubble_sorted = bubble_sort(percentages[:])  # Use a copy of the array
print("\nSorted Array (Bubble Sort):", bubble_sorted)

# Shell Sort
shell_sorted = shell_sort(percentages[:])  # Use a copy of the array
print("\nSorted Array (Shell Sort):", shell_sorted)
