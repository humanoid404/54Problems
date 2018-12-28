people = 8
pizzas = 2
pieces = 8
[people, pizzas, pieces] = [int(people), int(pizzas), int(pieces)]
each = (pizzas * pieces) / people
each = int(each)
leftover = pizzas * pieces - each * people
[people, pizzas, pieces, each, leftover] = [str(people), str(pizzas), str(pieces), str(each), str(leftover)]
print("How amny people? ", people)
print('How many pizzas do you have? ', pizzas)
print('How many pieces are in a pizza? ', pieces)
print(people, ' people with ', pizzas, ' pizzas')
print('Each person gets ', each, ' pieces of pizza.')
print('There are ', leftover, 'leftover pieces.')