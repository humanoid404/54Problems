while True:
    try:
        age = float(input("What is your age?\n"))
        if age < 0: raise ValueError
        print("You are {}old enough to legally drive.\n".format("not " if age < 16 else ""))
    except ValueError:
        print("Please enter a valid number.\n")
