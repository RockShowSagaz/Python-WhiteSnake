
def calculate(operation, num1, num2):
    if operation == "1":
        return num1 + num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"


assert calculate("1", 5, 3) == 8
assert calculate("1", -1, 1) == 0
assert calculate("1", 0, 0) == 0

assert calculate("2", 5, 3) == 2
assert calculate("2", -1, 1) == -2
assert calculate("2", 0, 0) == 0

assert calculate("3", 5, 3) == 15
assert calculate("3", -1, 1) == -1
assert calculate("3", 0, 5) == 0

assert calculate("4", 6, 3) == 2
assert calculate("4", -6, 3) == -2
assert calculate("4", 0, 5) == 0
assert calculate("4", 5, 0) == "Error: Division by zero"

assert calculate("5", 5, 3) == "Invalid operation"
assert calculate("0", 5, 3) == "Invalid operation"

print("All tests passed!")
