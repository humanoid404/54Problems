class Person:

    def __init__(self, first, last,income):
        self.first = first
        self.last = last
        # self.fullname = first + ', ' + last
        self.income=income
    # def __repr__(self):
        # return repr(self.first + ' ' + self.last)


#making a python file exercise42.py


import csv
import pandas as pd
#just read
f=open('exercise42.csv','r')
lines=f.readlines()



#make management list
person_list=[]


for x in lines:
    info=x.split(',')
    person_list.append(Person(info[0],info[1],int(info[2])))
    # print(info)
f.close()

data=[]
for per in person_list:
    t=[per.last,per.first,per.income]
    data.append(t)


#set index
k=0
index=[]
for i in range(len(data)):
    k+=1
    index.append(k)
#set columns
columns=['Last','First','Salary']

df = pd.DataFrame(data,columns=columns,index=index)
print(df)

