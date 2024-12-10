def union(x, y):
    r = x.copy()
    for i in y:
        if i not in r:
            r.append(i)
    return r

def intersection(x, y):
    r = []
    for i in x:
        if i in y:
            r.append(i)
    return r

def subtract(x, y):
    r = []
    for i in x:
        if i not in y:
            r.append(i)
    return r

n = int(input("Enter total number of students: "))

# Cricket players
a = []
n_a = int(input("Enter number of students who play Cricket: "))
print("Enter roll numbers of students who play Cricket:")
for i in range(n_a):
    x = int(input())
    a.append(x)

# Badminton players
b = []
n_b = int(input("Enter number of students who play Badminton: "))
print("Enter roll numbers of students who play Badminton:")
for i in range(n_b):
    x = int(input())
    b.append(x)

# Football players
c = []
n_c = int(input("Enter number of students who play Football: "))
print("Enter roll numbers of students who play Football:")
for i in range(n_c):
    x = int(input())
    c.append(x)

# Display results
print("The required lists are:")
print("Cricket:", a)
print("Badminton:", b)
print("Football:", c)

print("Students who play both Cricket and Badminton:", intersection(a, b))
print("Students who play either Cricket or Badminton but not both:", subtract(union(a, b), intersection(a, b)))
print("Number of students who play neither Cricket nor Badminton:", n - len(union(a, b)))
print("Students who play Cricket and Football but not Badminton:", subtract(intersection(a, c), b))
print("Students who do not play any game:", n - len(union(c, union(a, b))))
print("Students who play at least one game:", union(c, union(a, b)))
print("Students who play all games:", intersection(c, intersection(a, b)))
