import pandas as pd
import operator #2-dimension array sort


class Employee:

    def __init__(self, first, last, position, Separation_date):
        #         self.first=first
        #         self.last=last
        self.fullname = first + ' ' + last
        self.position = position
        self.Separation_date = Separation_date


#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

# prevent ugly representation.
#     def __repr__(self):
#         return repr((self.first + ' ' + self.last, self.position, self.Separation_date))


emp_1 = Employee('John', 'Johnson', 'Manager', '2016-12-31')
emp_2 = Employee('Jake', 'Jacobson', 'Programmer', ' ')
emp_3 = Employee('Thou', 'Xiong', 'Software Engineer', '2016-10-06')
emp_4 = Employee('Michaela', 'Michaelson', 'District Manager', '2015-12-19')
emp_5 = Employee('Jacquelyn', 'Jackson', 'DBA', '')

data = [[emp_1.fullname, emp_1.position, emp_1.Separation_date],
        [emp_2.fullname, emp_2.position, emp_2.Separation_date],
        [emp_3.fullname, emp_3.position, emp_3.Separation_date],
        [emp_4.fullname, emp_4.position, emp_4.Separation_date],
        [emp_5.fullname, emp_5.position, emp_5.Separation_date]]

# 기준을 무엇으로 정렬 할 것인가?

name = 0
position = 1
date = 2

data = sorted(data, key=operator.itemgetter(0))
# data=sorted(data,key=operator.itemgetter(2),reverse=True)

# set index
k = 0
index = []
for i in range(len(data)):
    k += 1
    index.append(k)
# set columns
columns = ['full name', 'position', 'Separation_date']

df = pd.DataFrame(data, columns=columns, index=index)
print(df)

