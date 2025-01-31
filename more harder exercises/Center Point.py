from math import sqrt, floor

def center_point(a, b, c, d):
    distance1 = sqrt(a ** 2 + b ** 2)
    distance2 = sqrt(c ** 2 + d ** 2)

    if distance1 > distance2:
        return f"({floor(c)}, {floor(d)})"
    return f"({floor(a)}, {floor(b)})"


a = float(input())
b = float(input())
c = float(input())
d = float(input())

print(center_point(a, b, c, d))
