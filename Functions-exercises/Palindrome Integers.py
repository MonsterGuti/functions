def is_palindrome(a):
    for num in a:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


string_numbers = input().split(", ")
is_palindrome(string_numbers)
