def input_polynomial():
    """Input a polynomial as a list of [coefficient, exponent]."""
    n = int(input("Enter the number of terms in the polynomial: "))
    poly = []
    for _ in range(n):
        coeff = float(input("Enter coefficient: "))  # Coefficient input
        exp = int(input("Enter exponent: "))        # Exponent input
        poly.append([coeff, exp])
    return poly


def display_polynomial(poly):
    """Display the polynomial in human-readable form."""
    terms = []
    for coeff, exp in poly:
        if exp == 0:
            terms.append(f"{coeff:.2f}")  # Display coefficient without x
        elif exp == 1:
            terms.append(f"{coeff:.2f}x")  # Display coefficient with x^1
        else:
            terms.append(f"{coeff:.2f}x^{exp}")  # Display coefficient with x^exp
    print(" + ".join(terms))


def evaluate_polynomial(poly, x):
    """Evaluate the polynomial for a given value of x."""
    result = 0
    for coeff, exp in poly:
        result += coeff * (x ** exp)
    return result


def add_polynomials(poly1, poly2):
    """Add two polynomials."""
    result = poly1.copy()
    for coeff2, exp2 in poly2:
        found = False
        for term in result:
            if term[1] == exp2:  # Exponent matches
                term[0] += coeff2
                found = True
                break
        if not found:
            result.append([coeff2, exp2])
    return sorted(result, key=lambda term: term[1], reverse=True)


def multiply_polynomials(poly1, poly2):
    """Multiply two polynomials."""
    result = []
    for coeff1, exp1 in poly1:
        for coeff2, exp2 in poly2:
            new_coeff = coeff1 * coeff2
            new_exp = exp1 + exp2
            for term in result:
                if term[1] == new_exp:
                    term[0] += new_coeff
                    break
            else:
                result.append([new_coeff, new_exp])
    return sorted(result, key=lambda term: term[1], reverse=True)


# Main Program
print("Polynomial Operations:")
print("1. Input and Output Polynomial")
print("2. Evaluate Polynomial")
print("3. Add Polynomials")
print("4. Multiply Polynomials")

choice = int(input("Enter your choice: "))

if choice == 1:
    poly = input_polynomial()
    print("The polynomial is:")
    display_polynomial(poly)

elif choice == 2:
    poly = input_polynomial()
    x = float(input("Enter the value of x: "))
    result = evaluate_polynomial(poly, x)
    print(f"The value of the polynomial at x={x} is: {result:.2f}")

elif choice == 3:
    print("Enter the first polynomial:")
    poly1 = input_polynomial()
    print("Enter the second polynomial:")
    poly2 = input_polynomial()
    result = add_polynomials(poly1, poly2)
    print("The sum of the polynomials is:")
    display_polynomial(result)

elif choice == 4:
    print("Enter the first polynomial:")
    poly1 = input_polynomial()
    print("Enter the second polynomial:")
    poly2 = input_polynomial()
    result = multiply_polynomials(poly1, poly2)
    print("The product of the polynomials is:")
    display_polynomial(result)

else:
    print("Invalid choice!")
