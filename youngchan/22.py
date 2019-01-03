acc = []  # accumulator list
max = None
n = 10  # number of inputs
i = 1  # loop counter

while not i > n:
    try:
        number = input("Enter the integer of order {}: ".format(i))
        number = int(number)
    except ValueError:
        if number == "":
            break
        else:
            print("\nPlease enter an integer.")
            continue
    if number in acc:
        print("You have already entered this integer. Try another one.")
        continue
    else:
        acc.append(number)
        if max is None:
            max = number
        else:
            max = number if number > max else max
    i += 1

if max is None:
    print("\nYou did not enter any number.")
else:
    print("\nThe largest number is {}.".format(max))
