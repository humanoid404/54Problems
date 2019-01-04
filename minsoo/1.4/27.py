def validateInput():
    while 1:
        first_name = input('Enter the first name: ')
        if len(first_name) == 0:
            print('The first name must be filled in.')
        elif 0 < len(first_name) < 2:
            print(f'"{first_name}" is not a valid first name. It is too short.')
        else:
            break
    while 1:
        last_name = input('Enter the last name: ')
        if len(last_name) == 0:
            print('The last name must be filled in.')
        elif 0 < len(last_name) < 2:
            print(f'"{last_name}"')
        else:
            break
    while 1:
        ZIP_code = input('Enter the ZIP code: ')
        if ZIP_code.isdigit() == 0:
            print('The ZIP code must be numeric.')
        else:
            break
    while 1:
        employee_ID = input('Enter an employee ID: ')
        A = employee_ID.split('-')
        if len(A) == 2 and A[0].isalpha() == 1 and A[1].isdigit() == 1 and len(A[0]) == 2 and len(A[1]) == 4:
            break
        else:
            print(f'{employee_ID} is not a valid ID.')
    print('There were no errors found.')
validateInput()

