#include <iostream>
#include <stack>
#include <string>
#include <algorithm> // For reverse

using namespace std;

// Function to check if parentheses are balanced
bool isWellParenthesized(const string& expression) {
    stack<char> s;
    for (char ch : expression) {
        if (ch == '(' || ch == '{' || ch == '[') {
            s.push(ch);
        } else if (ch == ')' || ch == '}' || ch == ']') {
            if (s.empty()) return false;
            char top = s.top();
            s.pop();
            if ((ch == ')' && top != '(') || 
                (ch == '}' && top != '{') || 
                (ch == ']' && top != '[')) {
                return false;
            }
        }
    }
    return s.empty();
}

// Function to check precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    if (op == '^') return 3;
    return 0;
}

// Function to convert infix to prefix
string infixToPrefix(const string& infix) {
    stack<char> operators;
    stack<string> operands;

    for (char ch : infix) {
        if (isalnum(ch)) {
            operands.push(string(1, ch)); // Push operands
        } else if (ch == '(') {
            operators.push(ch); // Push '('
        } else if (ch == ')') {
            // Process until '(' is found
            while (!operators.empty() && operators.top() != '(') {
                string op2 = operands.top(); operands.pop();
                string op1 = operands.top(); operands.pop();
                char op = operators.top(); operators.pop();
                operands.push(op + op1 + op2); // Prefix formation
            }
            operators.pop(); // Remove '('
        } else { 
            // Process operators
            while (!operators.empty() && precedence(operators.top()) >= precedence(ch)) {
                string op2 = operands.top(); operands.pop();
                string op1 = operands.top(); operands.pop();
                char op = operators.top(); operators.pop();
                operands.push(op + op1 + op2);
            }
            operators.push(ch); // Push current operator
        }
    }

    // Process remaining operators
    while (!operators.empty()) {
        string op2 = operands.top(); operands.pop();
        string op1 = operands.top(); operands.pop();
        char op = operators.top(); operators.pop();
        operands.push(op + op1 + op2);
    }

    return operands.top();
}

int main() {
    string expression;
    cout << "Enter an infix expression: ";
    cin >> expression;

    if (isWellParenthesized(expression)) {
        cout << "The expression is well-parenthesized.\n";
        string prefix = infixToPrefix(expression);
        cout << "Prefix expression: " << prefix << endl;
    } else {
        cout << "The expression is NOT well-parenthesized.\n";
    }

    return 0;
}