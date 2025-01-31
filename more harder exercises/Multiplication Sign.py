"""Try to do this WITHOUT multiplying the 3 numbers."""


def multiplication(a, b, c):
    if (a < 0 and (b > 0 and c > 0)) or (b < 0 and (a > 0 and c > 0)) or (c < 0 and (a > 0 and b > 0)) \
            or a < 0 and b < 0 and c < 0:
        return "negative"
    elif a == 0 or b == 0 or c == 0:
        return "zero"
    else:
        return "positive"


x = int(input())
y = int(input())
z = int(input())

print(multiplication(x, y, z))
