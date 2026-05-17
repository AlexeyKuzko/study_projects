"""Solution for Stepik course solutions: Algorithms Data Structures / 3 Basic Data Structures / 5 Stack / Step 8."""


def calculate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
    return stack.pop()


expression = input()
result = calculate_postfix(expression)
print(result)
