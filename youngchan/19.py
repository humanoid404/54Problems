while True:
    try:
        height = int(input("What is your height in inches: "))
        if not height > 0: raise ValueError
        weight = int(input("What is your weight in pounds: "))
        if not weight > 0: raise ValueError

        bmi = (weight/(height**2))*703
        print("Your BMI is ", bmi)

        if bmi < 18.5:
            print("You are underweight. Go consult a doctor.")
        elif 18.5 <= bmi < 25:
            print("You are within the ideal weight range.")
        else:
            print("You are underweight. Go consult a doctor.")
    except ValueError:
        print("Please enter a valid number.")
