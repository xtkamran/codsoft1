def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Welcome to Simple Calculator!")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = add(num1, num2)
    operation = "addition"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "subtraction"
elif choice == '3':
    result = multiply(num1, num2)
    operation = "multiplication"
elif choice == '4':
    result = divide(num1, num2)
    operation = "division"
else:
    print("Invalid input")
    exit()

if isinstance(result, float):
    print(f"The result of {num1} {operation} {num2} is: {result:.2f}")
else:
    print(result)
