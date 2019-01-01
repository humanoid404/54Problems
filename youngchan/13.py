while True:
    try:
        prompts = ["What is the principal amount?\n", "What is the rate in percentage?\n", "What is the number of years?\n", "What is the number of times the interest is compounded per year?\n"]
        principal, interestRate, years, compoundNumber = map(lambda s: float(input(s)), prompts)
        print("${} invested ar {}% for {} years compounded {} times per year is ${} .".format(principal, interestRate, years, compoundNumber, round(principal*(1+interestRate/(100*compoundNumber))**(compoundNumber*years), 2)))
        break
    except ValueError:
        print("Please enter a valid number.\n")
    except ZeroDivisionError:
        print("The numbers must be positive.\n")
