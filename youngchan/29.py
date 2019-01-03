while True:
    try:
        rate = float(input("What is the rate of return? "))
        print("It will take {} years to double your initial investment.\n".format(round(72/rate, 2)))
    except ValueError:
        print("\nPlease enter a valid number.")
    except ZeroDivisionError:
        print("\nThe rate must not be zero.")
