def orders(product, quantity):
    coffee_price = 1.50
    water_price = 1.00
    coke_price = 1.40
    snacks_price = 2.00
    result = None
    if product == "coffee":
        result = coffee_price * quantity
    elif product == "water":
        result = water_price * quantity
    elif product == "coke":
        result = coke_price * quantity
    elif product == "snacks":
        result = (snacks_price * quantity)
    print(f"{result:.2f}")


product = input()
quantity = float(input())
orders(product, quantity)
