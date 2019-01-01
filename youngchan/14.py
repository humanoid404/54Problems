while True:
    try:
        order = float(input("What is the order amount?\n"))
        state = input("What is the state?\n").upper()
        if state in ["WI", "WISCONSIN"]:
            prompt = "The subtotal is ${} .\nThe tax is ${} .\nThe total is ${} .".format(order, round(order*0.055, 2), round(order*1.055, 2))
        if state not in ["WI", "WISCONSIN"]:
            prompt = "The total is ${} .\n".format(order)
        print(prompt)
    except ValueError:
        print("Please enter a valid number.\n")
