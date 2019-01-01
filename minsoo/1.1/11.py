import math
rate_from = {'Euros': 137.51, '$': 100, 'KRW': 123, 'China': 111}
rate_to = {'Euros': 137.51, '$': 100, 'KRW': 123, 'China': 111}

A = {'Euros', '$', 'KRW', 'China'}
a = input('Which one do you want to exchange from? {}'.format(A))
b = input('Which one do you want to exchange to? {}'.format(A))
[a_rate_from, a_rate_to] = [rate_from[a], rate_to[b]]
ex_rate = float(a_rate_to) / float(a_rate_from)

print('The exchanging rate is {}.'.format(ex_rate))

amount_from = float(input("How many {} are you exchanging?".format(a)))

amount_to = math.ceil(float(amount_from) * float(a_rate_from) / float(a_rate_to))

print('{} {} at an exchanging rate of {} is {} {}'.format(amount_from, a, ex_rate, amount_to, b))

# [amount_from, a_rate_from, a_rate_to] = [float(input("How many {} are you exchanging?".format(a))), input("What is the exchanging rate?"), input('rate_to')]

# while type(amount_from) == 'float':
#     if 1:
#         break
#     else:
#         print("Input 'amount from' by 'float or int' type")
#
# while a_rate_from in rate_from:
#     a_rate_from = rate_from[a_rate_from]
#     break
# else:
#     print("'Rate from' is not defined")
#
# while a_rate_to in rate_to:
#     a_rate_to = rate_to[a_rate_to]
#     break
# else:
#     print("'Rate to' is not defined")

# a_amount_to = math.ceil(float(amount_from) * float(a_rate_from) / float(a_rate_to))
# print(a_amount_to)



# while (a_amount_from, a_rate_from, a_rate_to) in A:
#     a_amount_from = amount_from[a_amount_from]
#     a_rate_from = rate_from[a_amount_from]
#     a_rate_to = rate_to[a_rate_to]
#     a_amount_to = float(a_amount_from) * float(a_rate_from) / float(a_rate_to)
#     print(a_amount_from)
#     break
#
# else:
#     print("Amount of a is not defined")




# print('How many Euros are you exchanging? ', '{}'.format(amount_from))
# amount_to = float(amount_from) * float(rate_from) / float(rate_to)
# print('What is the exchange rate? ', amount_to)
# print(amount_from, ' Euros at an exchange rate of ', rate_from, ' is \n', amount_to, ' dollars')

# print(amount_from)