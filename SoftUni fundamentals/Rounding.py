def rounding(user_string):
    integer_list = []
    for char in user_string:
        number = float(char)
        number = round(number)
        integer_list.append(number)
    return integer_list


user_string = input().split()
print(rounding(user_string))
