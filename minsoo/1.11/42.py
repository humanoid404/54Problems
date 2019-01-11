f = open("C:/Users/wwnis/Desktop/42.txt", 'r')
A = []
i_0, i_1, i_2 = len('Last'), len('First'), len('Salary')
while 1:
    line = f.readline()
    if not line: break
    line_col = line.split(',')
    if i_0 < len(line_col[0]): i_0 = len(line_col[0])
    if i_1 < len(line_col[1]): i_1 = len(line_col[1])
    if i_2 < len(line_col[2]): i_2 = len(line_col[2])
    if line_col[-1][-1:] == '\n': line_col[-1] = line_col[-1][:-1]
    print(line_col)
    A.append(line_col)
B = sorted(A, key = lambda x: x[2])
B.reverse()
print('Last', ' '*(i_0  - len('Last')), 'First', ' '*(i_1 - len('First')), 'Salary', ' '*(i_2 - len('Salary')))
print('-'*(i_0 + i_1 + i_2 + 6))
for x in B:
    print(f'{x[0]}', ' '*(i_0 - len(x[0])), f'{x[1]}', ' '*(i_1 - len(x[1])), f'${int(x[2]):,}', ' '*(i_2 - len(x[2])))

# 이런 반법도 있다.
# def getKey(item):
#     return item[2]
# B = sorted(A, key = getKey)
# B.reverse()