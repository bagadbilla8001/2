def input_polynomial():
    """
    Function to input a polynomial and return it as a list of coefficients.
    """
    polynomial = list(map(int, input("Enter the polynomial coefficients (from highest to lowest power) separated by space: ").split()))
    return polynomial

def output_polynomial(coefficients):
    """
    Function to output the polynomial given the coefficients.
    """
    terms = []
    degree = len(coefficients) - 1
    for i, coef in enumerate(coefficients):
        if coef != 0:
            if degree - i == 0:
                terms.append(f"{coef}")
            elif degree - i == 1:
                terms.append(f"{coef}x")
            else:
                terms.append(f"{coef}x^{degree - i}")
    print("Polynomial:", " + ".join(terms))

def evaluate_polynomial(coefficients, x):
    """
    Function to evaluate a polynomial at a given value of x.
    """
    result = 0
    degree = len(coefficients) - 1
    for i, coef in enumerate(coefficients):
        result += coef * (x ** (degree - i))
    return result

def add_polynomials(p1, p2):
    """
    Function to add two polynomials.
    """
    # Making both polynomials the same length by padding with zeros
    max_len = max(len(p1), len(p2))
    p1 += [0] * (max_len - len(p1))
    p2 += [0] * (max_len - len(p2))
    
    result = [p1[i] + p2[i] for i in range(max_len)]
    return result

def multiply_polynomials(p1, p2):
    """
    Function to multiply two polynomials.
    """
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    return result

# Input: First Polynomial
print("Enter first polynomial:")
poly1 = input_polynomial()

# Input: Second Polynomial
print("Enter second polynomial:")
poly2 = input_polynomial()

# Output both polynomials
print("\nFirst Polynomial:")
output_polynomial(poly1)

print("\nSecond Polynomial:")
output_polynomial(poly2)

# Evaluate both polynomials at a given x
x_value = int(input("\nEnter the value of x to evaluate the polynomials: "))

result1 = evaluate_polynomial(poly1, x_value)
result2 = evaluate_polynomial(poly2, x_value)

print(f"\nFirst polynomial evaluated at x={x_value}: {result1}")
print(f"Second polynomial evaluated at x={x_value}: {result2}")

# Add polynomials
sum_poly = add_polynomials(poly1, poly2)
print("\nSum of the two polynomials:")
output_polynomial(sum_poly)

# Multiply polynomials
product_poly = multiply_polynomials(poly1, poly2)
print("\nProduct of the two polynomials:")
output_polynomial(product_poly)
