def perfect_number(a):
    num_sum = 0
    for n in range(1, a + 1):
        if a % int(n) == 0:
            num_sum += int(n)
    if num_sum == 2 * a:
        return "We have a perfect number!"
    return "It's not so perfect."


num = int(input())
print(perfect_number(num))
