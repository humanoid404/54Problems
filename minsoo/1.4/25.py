D = {1:'a very weak', 2:'a weak', 3:'a strong', 4:'a very strong', 0:'untyped'}

def passwordValidator(x):
    if f'{x}'.isdigit and len(f'{x}') < 8:
        return 1
    elif f'{x}'.isalpha() and len(f'{x}') < 8:
        return 2
    elif f'{x}'.isalnum() and f'{x}'.isalpha() == 0 and f'{x}'.isdigit() == 0 and len(f'{x}') >= 8:
        return 3
    elif f'{x}'.isalnum() == 0 and len(f'{x}') >= 8:
        return 4
    else:
        return 0

x = input('Enter your password')
passwordValidator(x)
print(f"The password '{x}' is {D[passwordValidator(x)]} password.")