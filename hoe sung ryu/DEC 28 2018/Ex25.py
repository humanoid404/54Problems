#EX25 <Password Strength Indicator>

# Ex25 fail ....try later

def passwordValidator(x):
    x = list(password)
    # 중간에 어캐 자르지
    s_alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z'}
    C_alpha = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z'}
    number = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    specialsymbol = {'~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '<', '>', '?', '|', ';', ':', ','}
    # {"'",'"'} 안됨
    # 숫자만
    set1 = number
    set2 = s_alpha
    set3 = s_alpha & number
    set4 = specialsymbol

    for i in x:
        if i in set1:
            if i in set2:
                if i in set4:
                    return 3
                else:
                    return 1
            else:
                return 0
        elif i in set2:
            if i in set1:
                if i in set4:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            pass


#     for i in x:
# #         if i in set1-(set2|set4):
#         if i in set1-(set2|set4):
#             if i in set2:
#                 if i in set4:
#                     return 3
#                 else:
#                     return 2
#             else:
#                 return 0

#         elif i in set2-(set1|set4):
#             return 1
# #         elif i in set3:
# #             return 2
# #         elif i in  set3 &set4:
# #             return 3

# unitypass= "".join(p)
pass_dic = {0: "The password '{0}' is a very weak password.", 1: "The password '{0}' is a weak password.",
            2: "The password '{0}' is a strong password.",
            3: "The password '{0}' is a very strong password."}

password = (input("input your password"))
print('-' * 40)
print(type(passwordValidator(password)))
print('-' * 40)
print(passwordValidator(password))
sencence = pass_dic.get(passwordValidator(password))
print('-' * 40)
print(type(sencence))
print('-' * 40)
print((sencence).format(password))


