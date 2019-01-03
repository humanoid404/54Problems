while True:
    try:
        times = int(input("How many numbers would you like to add? "))  # number of prompts
        if int(times) <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        print("\nPlease enter a positive integer.")


acc = 0  # accumulator
for i in range(times):
    try:
        number = int(input("Enter a number: "))
        acc += number
    except ValueError:
        continue
print("The total is {}.".format(acc))
