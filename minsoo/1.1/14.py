A = {'WI', 'NY', 'LA'}
B = {'WISCONSIN', 'NEW YORK', 'LOS ANGELES'}
amount = float(input('what is the order amount?'))
state = input('What is the state?')
r = 5.5
subtotal = amount
tax = 0.01 * r * amount
amount = amount * (1 + 0.01 * r)
if state.upper() in A or B:
    print("""The subtotal is ${:.2f}
The tax is ${:.2f}
The total is {:.2f}""".format(subtotal, tax, amount))
if state not in A:
    print('The total is ${:.2f}'.format(amount))