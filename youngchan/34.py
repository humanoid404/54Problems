employees = ["John Smith", "Jackie Jackson", "Chris Jones", "Jeremy Goodwin"]
name = ""
while employees:
    print("There are {} employees:".format(len(employees)))
    for i in employees:
        print(i)
    name = input("Enter an employee name to remove: ")
    if name == "exit":
        break
    elif name not in employees:
        print('\nThe name "{}" does not exist.'.format(name))
    else:
        employees.remove(name)
        print('')
