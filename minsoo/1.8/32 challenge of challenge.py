from random import randint as rd
c = 'y'
while c == 'y':
    D = {1: [k + 1 for k in range(10)], 2: [[10 * j + k + 1 for k in range(10)] for j in range(10)],
         3: [[[100 * i + 10 * j + k + 1 for k in range(10)] for j in range(10)] for i in range(10)]}
    I = [i1, i2, i3] = [rd(1, 10), rd(1, 100), rd(1, 1000)]
    i = 0
    a = 0
    while a not in [1,2,3]:
        a = input('Pick a difficulty level (1, 2, or 3): ')
        try:
            a = int(a)
        except: print('Invalid.')
    M = D[a]
    x = I[a-1]
    print(f'Answer is {x}')
    b = input(f"I have my number. What's your guess? Press a button in {M}")
    while b != x:
        i += 1
        try:
            b = int(b)
            if 0 < b < 10 ** a + 1:
                k = b % 10
                j = (b // 10) % 10
                i = (b // 100) % 10
                if a == 1:
                    if M[k-1] == 'Null':
                        print(f'You repeated the number {b}.')
                    else: M[k-1] = 'Null'
                elif a == 2:
                    if M[j][k-1] == 'Null':
                        print(f'You repeated the number {b}.')
                    else: M[j][k-1] = 'Null'
                else:
                    if M[i][j][k-1] == 'Null':
                        print(f'You repeated the number {b}.')
                    else: M[i][j][k-1] = 'Null'
            else: pass
            if b < x:
                print('Too low. Guess again: ')
                b = input(f'Press a button you guess in {M}')
            elif b > x:
                print('Too low. Guess again: ')
                b = input(f'Press a button you guess in {M}')
            else: pass
        except: b = input(f'Invalid Type. Press a button you guess in {M}')              # i -= 1 : 잘못 입력 카운트 안 하기
    if i == 1: print(f'You\'re a mind reader! You got it in {i} guesses!')
    elif 2<= i <5: print(f'Most impressive. You got it in {i} guesses!')
    elif 5<= i <7: print(f'You can do better than that. You got it in {i} guesses!')
    else: print(f'Better luck next time. You got it in {i} guesses!')
    while c != 'n':
        c = input('Play again? y/n ')
        if c.upper() in ['Y', 'N']:
            D = {'Y': "Let's play again!", 'N': 'Goodbye!'}
            print(f'{D[c.upper()]}')
            break
        else: print('Invalid.')

# A를 살린 코드
# from random import randint as rd
# c = 'y'
# while c == 'y':
#     D = {1: [k + 1 for k in range(10)], 2: [[10 * j + k + 1 for k in range(10)] for j in range(10)],
#          3: [[[100 * i + 10 * j + k + 1 for k in range(10)] for j in range(10)] for i in range(10)]}
#     A = set()
#     I = [i1, i2, i3] = [rd(1, 10), rd(1, 100), rd(1, 1000)]
#     i = 0
#     a = 0
#     while a not in [1,2,3]:
#         a = input('Pick a difficulty level (1, 2, or 3): ')
#         try:
#             a = int(a)
#         except: print('Invalid.')
#     M = D[a]
#     x = I[a-1]
#     print(f'Answer is {x}')
#     b = input(f"I have my number. What's your guess? Press a button in {M}")
#     while b != x:
#         i += 1
#         try:
#             b = int(b)
#             if 0 < b < 10 ** a + 1:
#                 k = b % 10
#                 j = (b // 10) % 10
#                 i = (b // 100) % 10
#                 if a == 1: M[k-1] = 'Null'
#                 elif a == 2: M[j][k-1] = 'Null'
#                 else: M[i][j][k-1] = 'Null'
#             else: pass
#             if b in A: print(f'You repeated the number {b}.')
#             else: pass
#             if b < x:
#                 A.add(b)
#                 print('Too low. Guess again: ')
#                 b = input(f'Press a button you guess in {M}')
#             elif b > x:
#                 A.add(b)
#                 print('Too low. Guess again: ')
#                 b = input(f'Press a button you guess in {M}')
#             else: pass
#         except: b = input(f'Invalid Type. Press a button you guess in {M}')              # i -= 1 : 잘못 입력 카운트 안 하기
#     if i == 1: print(f'You\'re a mind reader! You got it in {i} guesses!')
#     elif 2<= i <5: print(f'Most impressive. You got it in {i} guesses!')
#     elif 5<= i <7: print(f'You can do better than that. You got it in {i} guesses!')
#     else: print(f'Better luck next time. You got it in {i} guesses!')
#     while c != 'n':
#         c = input('Play again? y/n ')
#         if c.upper() in ['Y', 'N']:
#             D = {'Y': "Let's play again!", 'N': 'Goodbye!'}
#             print(f'{D[c.upper()]}')
#             break
#         else: print('Invalid.')