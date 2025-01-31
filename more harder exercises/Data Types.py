def transforming(a, b):
    if a == "int":
        return int(b) * 2
    elif a == "real":
        result = float(b) * 1.5
        return f"{(result):.2f}"
    elif a == "string":
        return f"${b}$"


command = input()
user_input = input()
print(transforming(command, user_input))
