def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    postfix = ''

    for char in expression:
        if char.isalpha():  # Operand
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remove the opening parenthesis '('
        else:  # Operator
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix


# Input
expression = input()

# Convert to postfix notation
postfix_expression = infix_to_postfix(expression)

# Output
print(postfix_expression)
