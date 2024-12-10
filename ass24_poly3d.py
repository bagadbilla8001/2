class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff  # Coefficient
        self.exp = exp      # Exponent
        self.next = None    # Pointer to the next node

class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coeff, exp):
        """Add a term to the polynomial."""
        new_node = Node(coeff, exp)
        if not self.head:
            self.head = new_node
        else:
            # Insert in descending order of exponent
            current = self.head
            while current.next and current.next.exp > exp:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        """Display the polynomial."""
        terms = []
        current = self.head
        while current:
            terms.append(f"{current.coeff}x^{current.exp}")
            current = current.next
        print(" + ".join(terms) if terms else "0")

    def evaluate(self, x):
        """Evaluate the polynomial at a given value of x."""
        result = 0
        current = self.head
        while current:
            result += current.coeff * (x ** current.exp)
            current = current.next
        return result

    def add(self, poly):
        """Add two polynomials."""
        result = Polynomial()
        current1 = self.head
        current2 = poly.head

        while current1 or current2:
            if current1 and (not current2 or current1.exp > current2.exp):
                result.add_term(current1.coeff, current1.exp)
                current1 = current1.next
            elif current2 and (not current1 or current2.exp > current1.exp):
                result.add_term(current2.coeff, current2.exp)
                current2 = current2.next
            else:  # current1.exp == current2.exp
                result.add_term(current1.coeff + current2.coeff, current1.exp)
                current1 = current1.next
                current2 = current2.next

        return result

# Input and Output of Polynomials
def input_polynomial():
    poly = Polynomial()
    n = int(input("Enter number of terms in polynomial: "))
    for _ in range(n):
        coeff, exp = map(int, input("Enter coefficient and exponent separated by space: ").split())
        poly.add_term(coeff, exp)
    return poly

def main():
    choice = 1
    while choice != 0:
        print("\n\n=========Polynomial Operations========\n")
        print("1. Input Polynomial")
        print("2. Display Polynomial")
        print("3. Evaluate Polynomial at a given value")
        print("4. Add Two Polynomials")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            poly = input_polynomial()
            print("Polynomial entered successfully.")

        elif choice == 2:
            poly.display()

        elif choice == 3:
            x = int(input("Enter value of x: "))
            result = poly.evaluate(x)
            print(f"Polynomial evaluated at x = {x} is {result}")

        elif choice == 4:
            poly2 = input_polynomial()
            result = poly.add(poly2)
            print("Sum of polynomials:")
            result.display()

        elif choice == 0:
            print("Exiting...")

if __name__ == "__main__":
    main()
