# Input marks
list = []
n = int(input("Enter the number of students: "))
for i in range(0, n):
    marks = int(input("Enter the marks of the student: "))
    while marks != -1 and (marks < 0 or marks > 50):
        print("You entered wrong marks. Re-enter the marks.")
        marks = int(input("Enter the marks of the student: "))
    list.append(marks)

# Absent students
def absent(list):
    count = 0
    for i in list:
        if i == -1:
            count += 1
    return count

# Maximum marks
def max_marks(list):
    max_val = list[0]
    for i in list:
        if i != -1 and i > max_val:
            max_val = i
    return max_val

# Minimum marks
def min_marks(list):
    min_val = list[0]
    for i in list:
        if i != -1 and i < min_val:
            min_val = i
    return min_val

# Sum of marks
def sum_marks(list):
    total = 0
    for i in list:
        if i != -1:
            total += i
    return total

# Average marks
def average(list):
    total_marks = sum_marks(list)
    valid_count = n - absent(list)
    return total_marks / valid_count if valid_count > 0 else 0

# Highest frequency
def frequency(list):
    counts = [0] * 5  # For ranges 1-10, 11-20, 21-30, 31-40, 41-50
    for i in list:
        if 1 <= i <= 10:
            counts[0] += 1
        elif 11 <= i <= 20:
            counts[1] += 1
        elif 21 <= i <= 30:
            counts[2] += 1
        elif 31 <= i <= 40:
            counts[3] += 1
        elif 41 <= i <= 50:
            counts[4] += 1
    return counts

print("Marks of the students are:", list)
print("No. of absent students are:", absent(list))
print("Maximum marks are:", max_marks(list))
print("Minimum marks are:", min_marks(list))
print("Average marks of all students are:", average(list))
print("Maximum frequency of marks is:", max(frequency(list)))
