'''Exercise 46 wordFrequency Finder'''


import re



f = open('46.txt', 'r')
data=f.read()
f.close


p = re.compile('[a-zA-Z]+')
compile_txt=p.findall(data)


words_set=set(compile_txt)

result_list=[]
for i in (words_set):

    num=0
    temp=[]
    for j in compile_txt:
        if i==j:
            num+=1
        else:
            pass
    temp.append(num)
    result_list.append({i:sum(temp)})

result_sorted = sorted(result_list, key = lambda x: [i for i in x.values()],reverse=True)

for i in (result_sorted):
    for key,value in i.items():
        print(key+':','*'*value)
