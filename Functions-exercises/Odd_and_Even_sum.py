def odd_and_even_sum(a):
    sum_of_even_digits = sum_of_odd_digits = 0
    for char in str(a):
        num = int(char)
        if num % 2 == 0:
            sum_of_even_digits += num
        elif num % 2 != 0:
            sum_of_odd_digits += num
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number = int(input())
print(odd_and_even_sum(number))
