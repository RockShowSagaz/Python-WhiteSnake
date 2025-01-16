print ("This is calculator")

print("Welcome to the Calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter the number of the operation (1/2/3/4): ")

if operation == "1":
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == "2":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == "3":
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation selected!")

    try:
        assert sum(2, 3) == 5, f"Klaida vykdant funkciją 'sum()'. Atsakymas turi būti {5}"
        assert sub(17, 10) == 7, f"Klaida vykdant funkciją 'sub()'. Atsakymas turi būti {7}"
        print(f'Visi testai yra sėkmingi')
    except AssertionError as klaida:
        print(f"Testas: {klaida}")
