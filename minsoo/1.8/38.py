a = input('Enter a list of numbers, separated by spaces: ')
y = ''
while 1:
    try:
        for x in a.split():
            try:
                x = int(x)
                if x % 2 == 0:
                    y = y + f'{x} '
            except: pass
        break
    except: a.pop()
print(y)
