def calculator(command, a, b):
    result = None
    if command == 'multiply':
        result = a * b
    elif command == "divide":
        result = int(a / b)
    elif command == "add":
        result = a + b
    elif command == "subtract":
        result = a - b
    return result


command = input()
a = int(input())
b = int(input())
print(calculator(command, a, b))
