B = {'NY':0.08, 'LA': 0.09, 'WI': 0.07}

res = input('Write your residence')
if res in B:
    res = B[res]
    sex = input('Write your sex. Man of Woman?')
    if sex.upper() == 'MAN':
        r = 0.6
    elif sex.upper() == 'WOMAN':
        r = 0.73
    else:
        print('Please state your sex correctly')
    A = float(input('Write your alcohol consumption'))
    W = float(input('Write your weight'))
    H = float(input('Write the elapsed time after drinking'))
    BAC = (A * 5.14 / (W * r)) - 0.15 * H
    if BAC >=res:
        print('''Your BAC is {}
It is not legal for you to drive.'''.format(BAC))
    elif BAC < res:
        print('''Your BAC is {}
It is legal for you to drive.'''.format(BAC))
else:
    print('Please state your residence correctly')