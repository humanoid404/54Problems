# [First Name, Last Name, Position, Separation Date], Null == ''
A = [['John', 'Johnson', 'Manager', '2016-12-32'],
     ['Tou', 'Xiong', 'Software Engineer', '2016-10-15'],
     ['Michaela', 'Michaelson', 'District Manager', '2015-12-19'],
     ['Jake', 'Jacobson', 'Programmer', ''],
     ['Jacquelyn', 'Jackson', 'DBA', ''],
     ['Sally', 'Weber', 'Web Developer', '2015-12-18']]
D = {}
L = []
B = []
for i in range(len(A)):
    D[A[i][1]] = i
    L.append(A[i][1])
L.sort()
for i in range(len(A)):
    B.append(A[D[L[i]]])
print('{:<20}| {:<20}| {:<20}'.format('Name', 'Position', 'Separation Date'))
print('-'*19, '|', '-'*19, '|','-'*20)
for x in B:
    y = x[0] +' ' + x[1]
    print(f'{y:<20}| {x[2]:<20}| {x[3]:20}')