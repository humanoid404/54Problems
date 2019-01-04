import math as m


def calculateMonthsUntilPaidOff(i, b, p):
    n = (-1 / 30) * (m.log10(1 + b / p * (1 - (1 + i) ** 30))) / (m.log10(1 + i))
    print(round(n, -1))


# n=flaot(input("the number of months"))
i_before = float(input("the daily rate"))
i = i_before * 0.01 / 365
b = float(input("the balance"))
p = float(input("the monthly payment"))

calculateMonthsUntilPaidOff(i, b, p)

