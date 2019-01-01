a = input(''' Press C convert from Fahrenheit to Celsius.
 Press F to convert from Celsious to Fahrenheit.''')

def f(x):
    return (x-32)*5/9, (x*9/5)+32   #[C=f(F), F=f(C)]

while a.upper() not in ['C', 'F']:
    print('You pressed the wrong button. Please press a correct button')
    a = input(''' Press C convert from Fahrenheit to Celsius.
 Press F to convert from Celsius to Fahrenheit.''')
else:
    print('Your choice: {}'.format(a.upper()))
    if a.upper() == 'C':
        F = float(input('Please enter the temperature in Fahrenheit: '))
        C = f(F)[0]
        print('The temperature in Celsius is {:.2f}.'.format(C))
    else:
        C = float(input('Please enter the temperature in Celsius: '))
        F = f(C)[1]
        print('The temperature in Fahrengeit: {:.2f}'.format(F))