def find_even(a):
    return int(a) % 2 == 0


string_numbers = input().split()
filtered_list = map(int, filter(find_even, string_numbers))
print(list(filtered_list))
