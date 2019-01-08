import random
A = []
a = input('Enter a name: ')
y = 'y'
while a:
    A.append(a)
    a = input('Enter a name: ')
while y == 'y':
    x = random.choice(A)
    print(f'The winner is... {x}')
    A.remove(x)
    if len(A) == 0:
        print('Everyone was awarded')
        break
    while 1:
        y = input('Do you want to assign other winner? y/n ')
        if y.upper() in ['Y', 'N']:
            break
        else: print('Invalid')
print('Finish the award.')