def cTOf(temp):
    return temp*9/5+32


def fTOc(temp):
    return (temp-32)*5/9


cTOk = lambda t: t+273.15
kTOc = lambda t: t-273.15
fTOk = lambda t: fTOc(t)+273.15
kTOf = lambda t: cTOf(t-273.15)


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
