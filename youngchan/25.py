from re import fullmatch

pwStrength = {-1: "undefined", 0: "empty", 1: "very weak", 2: "weak", 3: "strong", 4: "very strong"}

# -1=undefined, 0=empty, 1=very weak, 2=weak, 3=strong, 4=very strong
def pwValidator(pw):
    if len(pw) >= 8 and fullmatch(r".*[0-9].*", pw) and fullmatch(r".*[a-zA-Z].*", pw) and fullmatch(r".*[^\w\s].*", pw):
        return 4
    elif len(pw) >= 8 and fullmatch(r".*[0-9].*", pw) and fullmatch(r".*[a-zA-Z].*", pw):
        return 3
    elif len(pw) < 8 and fullmatch(r"[a-zA-Z]+", pw):
        return 2
    elif len(pw) < 8 and fullmatch(r"[0-9]+", pw):
        return 1
    elif not pw:
        return 0
    else:
        return -1

while True:
    pw = input("Enter password: ")
    print("The password '{}' is a {} password.\n".format(pw, pwStrength[pwValidator(pw)]))
