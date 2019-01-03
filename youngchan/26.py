from math import ceil, log1p


def calcMonthsUntilPaidOff(balance, apr, monthlyPayment):
    return (-1/30)*log1p(balance*(1-(1+apr/36500)**30)/monthlyPayment)/log1p(apr/36500)

while True:
    try:
        balance = float(input("What is your balance? "))
        apr = float(input("What is the APR on the card (as a percent)? "))
        monthlyPayment = float(input("What is the monthly payment you can make? "))
        print("It will take you {} months to pay off this card.\n".format(ceil(calcMonthsUntilPaidOff(balance, apr, monthlyPayment))))
    except ValueError:
        print("\nPlease enter a valid number.")
