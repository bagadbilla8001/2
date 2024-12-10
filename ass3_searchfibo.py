def linear_search(arr, target):
    """
    Function to perform linear search.
    Returns the index if the target is found, else returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def fibonacci_search(arr, target):
    """
    Function to perform Fibonacci search.
    Returns the index if the target is found, else returns -1.
    """
    n = len(arr)
    fib2 = 0  # (m-2)
    fib1 = 1  # (m-1)
    fib = fib1 + fib2  # (m)
    
    # Find the smallest Fibonacci number greater than or equal to the length of the array
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    
    offset = -1
    
    # Perform the Fibonacci search
    while fib > 1:
        i = min(offset + fib2, n - 1)
        
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        
        else:
            return i  # Target found at index i
    
    # Check the last possible position
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1  # Target found at index offset + 1
    
    return -1  # Target not found


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

# Perform Linear Search on the original list
linear_index = linear_search(roll_numbers, search_roll)

# Perform Fibonacci Search on the sorted list
fib_index = fibonacci_search(sorted_roll_numbers, search_roll)

# Display the results
if linear_index != -1:
    print(f"Roll number {search_roll} attended the training program (found in original list at index {linear_index}).")
else:
    print(f"Roll number {search_roll} did not attend the training program (not found in original list).")

if fib_index != -1:
    print(f"Roll number {search_roll} attended the training program (found in sorted list at index {fib_index}).")
else:
    print(f"Roll number {search_roll} did not attend the training program (not found in sorted list).")
