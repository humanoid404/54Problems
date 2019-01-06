D = {1:'a very weak', 2:'a weak', 3:'a strong', 4:'a very strong', 0:'untyped'}

def passwordValidator():
    if len(x) < 8 and x.isnumeric():
        return 1
    elif len(x) < 8 and x.isalpha():
        return 2
    elif len(x) >= 8 and x.isalnum() and x.isalpha() == 0 and x.isnumeric() == 0:
        return 3
    elif len(x) >= 8 and x.isalnum() == 0:
        return 4
    else:
        return 0

x = input('Enter your password')
passwordValidator()
print(f"The password '{x}' is {D[passwordValidator()]} password.")
