A = {'id1': 'pw1', 'id2': 'pw2', 'id3': 'pw3'}

a = input('Write your id')


if a not in A:
    print('There is no account like that')
else:
    pw = input('What is your password: ')
    if pw == A[a]:
        print('Welcome')
    else:
        print('That password is incorrect.')
