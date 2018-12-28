#Exercise8-1


ppl=int(input('How many people?'))
pizzas=int(input("how many pizzas do you have"))
each=int(input("How many pieces each person eat?"))
num_p=8*pizzas
left_p=num_p%int(ppl*each)
print('{0} people with {1} pizzas'.format(ppl,pizzas))
print('Each person gets %d pieces of pizza.' %each)
print('There are %d leftover pieces' %left_p)