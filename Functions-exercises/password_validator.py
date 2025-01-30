def password_validator(a):
    errors = []

    if len(a) < 6 or len(a) > 10:
        errors.append("Password must be between 6 and 10 characters")
    if not a.isalnum():
        errors.append("Password must consist only of letters and digits")

    digit_count = sum(1 for char in a if char.isdigit())
    if digit_count < 2:
        errors.append("Password must have at least 2 digits")

    if errors:
        return "\n".join(errors)
    return "Password is valid"


password = input()
print(password_validator(password))
