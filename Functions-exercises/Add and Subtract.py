def add_and_subtract(a, b, c):
    def sum_numbers():
        return a + b

    def subtract():
        result = sum_numbers()
        return result - c

    final_result = subtract()
    return final_result


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
