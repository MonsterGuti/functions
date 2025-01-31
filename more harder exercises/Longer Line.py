from math import sqrt, floor


def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def order_by_proximity(x1, y1, x2, y2):
    distance1 = sqrt(x1 ** 2 + y1 ** 2)
    distance2 = sqrt(x2 ** 2 + y2 ** 2)

    if distance1 <= distance2:
        return x1, y1, x2, y2
    else:
        return x2, y2, x1, y1


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
x4, y4 = float(input()), float(input())

line1_length = calculate_distance(x1, y1, x2, y2)
line2_length = calculate_distance(x3, y3, x4, y4)

if line1_length >= line2_length:
    x1, y1, x2, y2 = order_by_proximity(x1, y1, x2, y2)
else:
    x1, y1, x2, y2 = order_by_proximity(x3, y3, x4, y4)

print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
