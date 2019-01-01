P = input('Enter the principal')
r = input('Enter the rate of interest( %)')
t = input('Enter the number of years')

while 1:
    if [type(P), type(r), type(t)] != [float, float, float]:
        try:
            [P, r, t] = [float(P), float(r), float(t)]
            # print([type(P), type(r), type(t)])
        except:
            print('Please enter the numeric values.')
            P = input('Enter the principal')
            r = input('Enter the rate of interest( %)')
            t = input('Enter the number of years')
    else:
        break

A = float(P)*(1+0.01*float(r)*float(t))
print('After {} years at {}%, the investment will be worth ${:.2f}'.format(t, r, A))