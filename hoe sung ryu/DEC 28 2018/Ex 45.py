import re


# readline_all.py

f = open('46.txt', 'r')
data=f.read()
f.close
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()


p = re.compile('[a-zA-Z]+')
# data="the the the the badger badger."
# data="The play opens amid thunder and lightning, and the Three Witches decide"
compile_txt=p.findall(data)


# print(compile_txt)
words_set=set(compile_txt)
# print(words_set)

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


for i in (result_list):
    for key,value in i.items():
        print(key+':','*'*value)


##