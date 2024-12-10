def sentinel_search(arr, target):
    """
    Function to perform Sentinel Search.
    Returns the index if the target is found, else returns -1.
    """
    n = len(arr)
    last = arr[-1]
    arr[-1] = target  # Place the target as the sentinel

    i = 0
    while arr[i] != target:
        i += 1

    arr[-1] = last  # Restore the last element
    if i < n - 1 or arr[-1] == target:
        return i
    return -1


def binary_search(arr, target):
    """
    Function to perform Binary Search.
    Returns the index if the target is found, else returns -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input: Roll numbers in random order
roll_numbers = list(map(int, input("Enter roll numbers of students (space-separated): ").split()))

# Create a sorted copy of the roll numbers
sorted_roll_numbers = sorted(roll_numbers)

print("\nOriginal Roll Numbers:")
print(roll_numbers)

print("\nSorted Roll Numbers:")
print(sorted_roll_numbers)

# Input: Roll number to search
search_roll = int(input("\nEnter the roll number to search: "))

# Perform Sentinel Search on the original list
sentinel_index = sentinel_search(roll_numbers, search_roll)

# Perform Binary Search on the sorted list
binary_index = binary_search(sorted_roll_numbers, search_roll)

# Display the results
if sentinel_index != -1:
    print(f"Roll number {search_roll} attended the training program (found in original list at index {sentinel_index}).")
else:
    print(f"Roll number {search_roll} did not attend the training program (not found in original list).")

if binary_index != -1:
    print(f"Roll number {search_roll} attended the training program (found in sorted list at index {binary_index}).")
else:
    print(f"Roll number {search_roll} did not attend the training program (not found in sorted list).")
