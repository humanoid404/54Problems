# [First Name, Last Name, Position, Separation Date], Null == ''
A = [['John', 'Johnson', 'Manager', '2016-12-32'],
     ['Tou', 'Xiong', 'Software Engineer', '2016-10-15'],
     ['Michaela', 'Michaelson', 'District Manager', '2015-12-19'],
     ['Jake', 'Jacobson', 'Programmer', ''],
     ['Jacquelyn', 'Jackson', 'DBA', ''],
     ['Sally', 'Weber', 'Web Developer', '2015-12-18']]

# Name
a = input('Enter a search string in Name: ')
B = set()                                                                   # First Name과 Last Name의 중복은 하나로 취급하므로 set()으로 작성.
for k in range(2):
     for x in A:
          if len(x[k]) > len(a):
              for j in range(len(x[k]) - len(a)):
                   if a == x[k][j:j+len(a)]:
                        B.add(A.index(x))
                        break
          elif len(x[k]) == len(a):
               if a == x[k]:
                    B.add(A.index(x))
print('Results: ')
print('{:<20}| {:<20}| {:<20}'.format('Name', 'Position', 'Separation Date'))
print('-'*19, '|', '-'*19, '|','-'*20)
for x in list(B):
    y = A[x][0] +' ' + A[x][1]
    print(f'{y:<20}| {A[x][2]:<20}| {A[x][3]:20}')

# Position
a = input('Enter a search string in Position: ')
print('Results: ')
print('{:<20}| {:<20}| {:<20}'.format('Name', 'Position', 'Separation Date'))
print('-'*19, '|', '-'*19, '|','-'*20)
for x in A:
    if len(x[2]) > len(a):
        for j in range(len(x[2]) - len(a)):
            if a == x[2][j:j+len(a)]:
                y = x[0] + ' ' + x[1]
                print(f'{y:<20}| {x[2]:<20}| {x[3]:20}')
                break
    elif len(x[k]) == len(a):
        if a == x[k]:
            y = x[0] + ' ' + x[1]
            print(f'{y:<20}| {x[2]:<20}| {x[3]:20}')

# Separation date
a = input('Enter the months from today: ')
print('Results: ')
print('{:<20}| {:<20}| {:<20}'.format('Name', 'Position', 'Separation Date'))
print('-'*19, '|', '-'*19, '|','-'*20)
from datetime import date
from dateutil.relativedelta import relativedelta                            # python-dateutil module 사용
time = str(date.today() + relativedelta(months = -int(a)))
for x in A:
    if len(x[3]) == 0:
        continue
    elif x[3] <= time:
        y = x[0] + ' ' + x[1]
        print(f'{y:<20}| {x[2]:<20}| {x[3]:20}')
