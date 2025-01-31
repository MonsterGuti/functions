def loading_bar(a):
    percents = a // 10
    points = 10 - percents
    loading_string = "%" * percents + "." * points
    if a != 100:
        return f"{a}% [{loading_string}]\nStill loading..."
    return f"100% Complete!\n[{loading_string}]"


number = int(input())
print(loading_bar(number))
