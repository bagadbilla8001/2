#include <iostream>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

// Function to convert postfix to infix
string postfixToInfix(string postfix) {
    stack<string> s;
    for (char c : postfix) {
        if (isalnum(c)) {  // If the character is an operand
            s.push(string(1, c));  // Push it onto the stack as a string
        } else {  // Operator encountered
            string op2 = s.top(); s.pop();  // Pop the top element (operand)
            string op1 = s.top(); s.pop();  // Pop the next top element (operand)
            string expr = "(" + op1 + c + op2 + ")";  // Form the expression
            s.push(expr);  // Push the formed expression back to the stack
        }
    }
    return s.top();  // The final element in the stack is the result
}

// Function to convert postfix to prefix
string postfixToPrefix(string postfix) {
    stack<string> s;
    reverse(postfix.begin(), postfix.end());  // Reverse the postfix expression
    for (char c : postfix) {
        if (isalnum(c)) {  // If the character is an operand
            s.push(string(1, c));  // Push it onto the stack as a string
        } else {  // Operator encountered
            string op1 = s.top(); s.pop();  // Pop the top element (operand)
            string op2 = s.top(); s.pop();  // Pop the next top element (operand)
            string expr = c + op1 + op2;  // Form the expression
            s.push(expr);  // Push the formed expression back to the stack
        }
    }
    return s.top();  // The final element in the stack is the result
}

int main() {
    string postfix;
    int choice;

    do {
        cout << "\n\n=========Postfix Expression Conversions========\n";
        cout << "1. Postfix to Infix\n2. Postfix to Prefix\n0. Exit\nEnter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter postfix expression: ";
            cin >> postfix;
            cout << "Infix expression: " << postfixToInfix(postfix) << endl;
        } else if (choice == 2) {
            cout << "Enter postfix expression: ";
            cin >> postfix;
            cout << "Prefix expression: " << postfixToPrefix(postfix) << endl;
        } else if (choice == 0) {
            break;
        } else {
            cout << "Invalid choice! Please try again.\n";
        }
    } while (true);

    return 0;
}
