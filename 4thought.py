from itertools import product
def find_expression(n):
    ops = ["+", "-", "*", "//"]
    for op1, op2, op3 in product(ops, ops, ops):
        expression = f"4 {op1} 4 {op2} 4 {op3} 4"
        try:
            if eval(expression) == n:
                return expression.replace('//', '/')
        except ZeroDivisionError:
            pass
    return "no solution"

# Input
num_test_cases = int(input())
test_cases = [int(input()) for _ in range(num_test_cases)]

# Output
for case in test_cases:
    result = find_expression(case)
    if result != "no solution":
        print(result + " = " + str(case))
    else:
        print(result)
