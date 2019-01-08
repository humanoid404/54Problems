A = ['John Smith', 'Jackie jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']
j = 0
while j in range(2):
    j += 1
    print(f'There are {len(A)} employees: ')
    for i in A:
        print(i)
    if j == 2: break
    name = input('Enter an employee name to remove: ')
    try:
        A.remove(name)
    except:
        print(f'{name} is not an employee.')
        j += 1