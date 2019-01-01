def cTOf(t): return t*9/5+32
def fTOc(t): return (t-32)*5/9
def cTOk(t): return t+273.15
def kTOc(t): return t-273.15
def fTOk(t): return fTOc(t)+273.15
def kTOf(t): return cTOf(t-273.15)


tempNames = {"F": "Fahrenheit",
             "C": "Celsius",
             "K": "Kelvin"}

converts = {"FC": fTOc,
            "CF": cTOf,
            "CK": cTOk,
            "KC": kTOc,
            "FK": fTOk,
            "KF": kTOf}

while True:
    try:
        for key in tempNames:
            notKey = [tempNames[x] for x in tempNames if x != key]
            print("Press {} to convert from {} to {} and {}.".format(key, tempNames[key], *notKey))
        choice = input().strip().upper()[0]
        if choice not in tempNames: raise ValueError
        temp = input("Please enter the temperature in {}:\n".format(tempNames[choice]))
        temp = float(temp)
        for tName in tempNames:
            if tName == choice: continue
            print("The temperature in {} is {} .".format(tName, (converts[choice+tName])(temp)))
    except ValueError:
        print("Please enter a valid input.\n")
