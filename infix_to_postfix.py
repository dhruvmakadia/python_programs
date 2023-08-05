def precedence(operator):
    precedence_dict = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    return precedence_dict.get(operator, 0)


def infix_to_postfix(expression):
    output = []
    operator_stack = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while operator_stack and precedence(operator_stack[-1]) >= precedence(char):
                output.append(operator_stack.pop())
            operator_stack.append(char)

    while operator_stack:
        output.append(operator_stack.pop())

    return ''.join(output)


if __name__ == "__main__":
    user_input = input("Enter the infix expression: ")
    postfix_expression = infix_to_postfix(user_input)
    print("Postfix expression:", postfix_expression)
