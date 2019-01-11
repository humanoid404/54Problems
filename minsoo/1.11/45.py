f = open('C:/Users/wwnis/Desktop/45.txt', 'r')
A = []
k = 0
while 1:
    line = f.readline()
    if not line: break
    for i in range(len(line) - len('utilize')):
        if line[i:i+7] == 'utilize':
            line = line[:i] + 'use' + line[i + 7:]
            k += 1
    A.append(line)
f.close()
f = open('C:/Users/wwnis/Desktop/45_new.txt', 'w')
for i in range(len(A)):
    data = A[i]
    f.write(data)
f.close()
print(f"Total {k} revisions" )