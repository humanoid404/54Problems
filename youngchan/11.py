while True:
    try:
        prompts = ["How many euros are you exchanging?\n", "What is the exchange rate?\n"]
        euros, exchangeRate = map(lambda s: float(input(s)), prompts)
        dollars = round(euros*exchangeRate, 2)
        print("{} euros at an exchange rate of {} is {} U.S. dollars.".format(euros, exchangeRate, dollars))
        break
    except ValueError:
        print("Please enter a valid number.\n")
