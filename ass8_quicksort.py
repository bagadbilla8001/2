def quick_sort(arr):
    """
    Function to sort an array using Quick Sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the pivot element
        left = [x for x in arr if x < pivot]  # Elements less than pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x > pivot]  # Elements greater than pivot
        return quick_sort(left) + middle + quick_sort(right)


def display_top_five(scores):
    """
    Function to display the top five scores from a sorted list.
    """
    print("Top 5 Scores (Highest to Lowest):")
    for i in range(5):  # Access last 5 elements in reverse order
        print(f"{i}. {scores[len(scores)-i-1]:.2f}")


# Input: First year percentages
# percentages = [82.5, 91.2, 79.8, 67.3, 85.6, 90.1, 76.4, 92.7, 88.3, 94.0, 72.8, 80.9]

# print("Original Percentages:")
# print(percentages)

# Sorting using Quick Sort
lan = list(map(int,input("Enter the array to be sorted").split()))

sorted_percentages = quick_sort(lan)

print("\nSorted Percentages (Ascending Order):")
print(sorted_percentages)

# Display the top five scores
display_top_five(sorted_percentages)