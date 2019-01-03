while True:
    try:
        orderAmount = float(input("What is the order amount? "))
        state = input("What state do you love in? ").upper()
        if state in ["WI", "WISCONSIN"]:
            taxRate = 0.05
            county = input("Enter the county of residence: ").upper()
            if county in ["EAU CLAIRE"]:
                taxRate += 0.005
            elif county in ["DUNN"]:
                taxRate += 0.004
        elif state in ["ILLINOIS"]:
            taxRate = 0.08
        else:
            taxRate = 0
        print("The tax is $", round(orderAmount*taxRate, 2),
              "\nThe total is $", round(orderAmount*(1+taxRate), 2))
    except ValueError:
        print("Please enter a valid number.")
