'''Exercise35 Picking a Winner '''



# import random as r
# name=[]
# while True:
#     try:
#         if t=='':
#             break
#         else:
#             # name.append(str(input("Enter a name: ")))
#             t = str(input("Enter a name: "))
#             name.append(t)
#             continue
#     except:
#         continue
#
#
# ran_win_num = r.randint(0, len(name) - 1)
# print(f"The winner is ...{name[ran_win_num]}")
# # print(name)
# del name[ran_win_num]
# # print(name)
# second_ran_win_num=r.randint(0,len(name)-1)
# print(f"The second winner is ...{name[second_ran_win_num]}")


import random as r

name=[]
t=0
while True:
    try:
        if t=='':
            ran_win_num = r.randint(0, len(name) - 1)
            print(f"The winner is ...{name[ran_win_num]}")
            break
        elif t!='':
            t = str(input("Enter a name: "))
            name.append(t)
            continue
    except:
        pass

