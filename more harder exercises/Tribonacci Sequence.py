def tribonacci(a):
    tribonacci_numbers = [1, 1, 2]
    for i in range(a - 3):
        tribonacci_numbers.append(sum(tribonacci_numbers[-3:]))
    return " ".join(map(str, tribonacci_numbers[:a]))


num = int(input())
print(tribonacci(num))
