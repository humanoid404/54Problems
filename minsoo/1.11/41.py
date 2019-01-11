f = open("C:/Users/wwnis/Desktop/41.txt", 'r')
A = []
while 1:
    line = f.readline()
    if not line: break
    if line[-1:] != '\n': line += '\n'
    A.append(line)
A.sort()
A[-1] = A[-1][:-1]
print(f'Total of {len(A)} names')
print('-'*20)
print(''.join(A))
f.close()
f = open("C:/Users/wwnis/Desktop/41_new.txt", 'w')
for i in range(len(A)):
    data = A[i]
    f.write(data)
f.close()