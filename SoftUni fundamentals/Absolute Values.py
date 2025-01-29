def abs_values():
    user_input = input().split()
    float_list = []
    for char in user_input:
        number = float(char)
        float_list.append(abs(number))
    print(float_list)

abs_values()
