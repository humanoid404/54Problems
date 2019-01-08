'''Ex34 Employee List Removal'''



employee_list=['John Smith','Jackoe Jackson','Chris Jones','Amanda cullen','Jeremy Goodwin']

print(f"There are {len(employee_list)} employees:")
for e in employee_list:
    print(e)

while True:
    try:
        remove_employee=input("Enter an employee name to remove")
        employee_list.remove(remove_employee)
        print(f"There are {len(employee_list)} employees:")
        for e in employee_list:
            print(e)
        break

    except:
        print("please input valid name")

# a = [1, 2, 3, 4, 5, 6, 7]
# del a[a.index(3)] or a.remove(3)
     #소문자 대문자 상관 없이 쳐도 되고 빈칸 무시해도 되는거 만들기