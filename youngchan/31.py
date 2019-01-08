def targetHR(restingHR, age, intensity):
    return round(((220-age-restingHR)*intensity)+restingHR)


while True:
    try:
        restingHR = float(input("Resting Pulse: "))
        age = float(input("Age: "))
        print("Intensity\t|\tRate")
        print("----------------|-------------")
        for i in range(55, 96, 5):
            print("{}%\t\t|\t{}bpm".format(i, targetHR(restingHR, age, i/100)))
    except ValueError:
        print("\nPlease enter a valid number")
