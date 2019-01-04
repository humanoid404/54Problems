i = 0
while 1:
    r = input('What is the rate of return? ')
    try:
        r = float(r)
        y = 72/r
        break
    except ZeroDivisionError:
        i += 1
        if i % 4 == 1:
            print("Sorry. That's not a valid input.")
        elif i % 4 == 2:
            print('r이 0이면 안돼')
        elif i % 4 == 3:
            print('0으로 나누면 안 된다고')
        elif i % 4 == 0:
            print('안돼 돌아가')
    except ValueError:
        print('r must be numeric')

print(f'It will take {y:.2f} years to double your initial investment.')