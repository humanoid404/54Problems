from math import floor, ceil


def calculateSimpleInterest(principal, interestRate, years):
    return round(principal*(1+interestRate*years/100), 2)


while True:
    try:
        prompts = ["Enter the principal:\n", "Enter the rate of interest in percentage:\n", "Enter the number of years:\n"]
        principal, interestRate, years = map(lambda s: float(input(s)), prompts)
        for y in range(0, 1+floor(years)):
            print("After {} years at {}%, the investment will be worth ${} .".format(y, interestRate, calculateSimpleInterest(principal, interestRate, y)))
        if ceil(years) != floor(years):
            print("After {} years at {}%, the investment will be worth ${} .".format(years, interestRate, calculateSimpleInterest(principal, interestRate, years)))
        break
    except ValueError:
        print("Please enter a valid number.\n")
