S = 0

while 1:
    n = input('Enter the number of inputs? ')
    try:
        n = int(n)
        break
    except:
        print('Invalid')

for i in range(n):
    a = input('Enter a number:')
    try:
        a = int(a)
        S += a
    except:
        print('Invalid')
print(f'The total is {S}.')