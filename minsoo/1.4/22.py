# A = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
A = ['1st']
S = []
M = 0
k = 1
for i in A:
    while k:
        n = input(f'Enter the {i} number or "finish": ')
        if n == 'finish':
            k = 0
            break
        else:
            if len(A) % 10 == 0:
                s = f'{len(A) + 1}st'
            elif len(A) % 10 == 1:
                s = f'{len(A) + 1}nd'
            elif len(A) % 10 == 2:
                s = f'{len(A) + 1}rd'
            else:
                s = f'{len(A) + 1}th'
            A.append(s)
        try:
            j = int(n)
            if j in S:
                k = 0
                break
            else:
                S.append(j)
                if j < M:
                    break
                elif j > M:
                    M = j
                    break
                else:
                    print('Maximum number error')
                    break
        except:
            print('Invalid.')

if len(A) == 1:
    print('You did not enter any number')
elif n == 'finish':
    print(f'The largest number is {M}.')
else:
    print('You enter a repeated number. Shut down')