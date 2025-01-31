def factorial(a, b):
    final_num = 1.0
    for num in range(b + 1, a + 1):
        final_num *= num
    return f"{(final_num):.2f}"


a = int(input())
b = int(input())
print(factorial(a, b))

