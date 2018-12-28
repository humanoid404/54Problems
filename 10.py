import re

patternBill = re.compile(r' *\$* *(\d+(\.\d\d)?) *\$* *')
patternNonnegativeInteger = re.compile(r"\d+")

subtotal = 0
itemNumber = 1
while True:
    while True:
        price = input("Enter the price of item {} in dollars.\nEnter 0 to end loop.\n".format(itemNumber))
        if not re.fullmatch(patternBill, price):
            print("\nPlease enter a valid price in dollars.")
        else:
            price = float(price)
            break
    if price == 0: break
    while True:
        quantity = input("Enter the quantity of item {}.\nEnter 0 to end loop.\n".format(itemNumber))
        if not re.fullmatch(patternNonnegativeInteger, quantity):
            print("\nPlease enter a nonnegative integer.")
        else:
            quantity = float(quantity)
            break
    if quantity == 0: break
    subtotal = round(subtotal+price*quantity, 2)
    itemNumber += 1
    print("")

print("""Subtotal: ${}
Tax: ${}
Total: ${}""". format(subtotal, round(subtotal*0.055, 2), round(subtotal*1.055, 2)))
