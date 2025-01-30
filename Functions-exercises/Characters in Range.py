def characters_in_range(a, b):
    char_list = []
    for char_index in range(ord(a) + 1, ord(b), 1):
        char_list.append(chr(char_index))
    return " ".join(char_list)


first_char = input()
second_char = input()
print(characters_in_range(first_char, second_char))
