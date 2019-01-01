W = {'WI', 'WISCONSIN'}
I = {'ILLINOIS', 'IL'}
W1 = {'EAU CLAIRE': 0.5, 'DUNN': 0.4}
amount = float(input('What is the order amount?'))
state = input('What state do you live in?')
if state.upper() in I:
    r = 8
    print('''"The state tax is ${:.2f}"
"The total tax is ${:.2f}"
"The total is ${:.2f}"'''.format(amount*0.01*r, amount*0.01*r, amount*(1+0.01*r)))
elif state.upper() in W:
    r = 5.5
    county = input('What county do you live in?')
    if county.upper() in W1:
        r1 = float(W1[county.upper()])
        r2 = r + r1
        print('''"The state tax is ${:.2f}"
"The county tax is ${:.2f}"
"The total tax is ${:.2f}"
"The total is ${:.2f}"'''.format(amount*0.01*r, amount*0.01*r1, amount*0.01*r2, amount*(1+0.01*r2)))
    if county.upper() not in W1:
        print('''"The state tax is ${:.2f}"
"The total tax is ${:.2f}"
"The total is ${:.2f}"'''.format(amount * 0.01 * r, amount * 0.01 * r, amount * (1 + 0.01 * r)))
else:
    r = 5.5
    print('''"The total is ${:.2f}"'''.format(amount*(1+0.01*r)))


# # challenge 마지막
# W = {'WI', 'WISCONSIN'}
# I = {'ILLINOIS', 'IL'}
# W1 = {'EAU CLAIRE': 0.5, 'DUNN': 0.4}
# amount = float(input('What is the order amount?'))
# state = input('What state do you live in?')
# county = input('What county do you live in?')
# if state.upper() in I:
#     r = 8
#     print('''"The state tax is ${:.2f}"
# "The total tax is ${:.2f}"
# "The total is ${:.2f}"'''.format(amount*0.01*r, amount*0.01*r, amount*(1+0.01*r)))
# elif state.upper() in W and county.upper() in W1:
#     r = 5.5
#     r1 = float(W1[county.upper()])
#     r2 = r + r1
#     print('''"The state tax is ${:.2f}"
# "The county tax is ${:.2f}"
# "The total tax is ${:.2f}"
# "The total is ${:.2f}"'''.format(amount*0.01*r, amount*0.01*r1, amount*0.01*r2, amount*(1+0.01*r2)))
# elif state.upper() in W and county.upper() not in W1:
#     r = 5.5
#     print('''"The state tax is ${:.2f}"
# "The total tax is ${:.2f}"
# "The total is ${:.2f}"'''.format(amount * 0.01 * r, amount * 0.01 * r, amount * (1 + 0.01 * r)))
# else:
#     r = 5.5
#     print('''"The total is ${:.2f}"'''.format(amount*(1+0.01*r)))