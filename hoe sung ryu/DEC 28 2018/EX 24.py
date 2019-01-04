#
def isAnagram(x ,y):
    x_list =list(x)
    y_list =list(y)
    #value=잘못된 문자(i)와 key=위치(n) dictionary
    w_dic={}
    if len(x_list)==len(y_list):
        n = -1 # find wrong position
        T = 0 # 맞는게 몇개인가
        w_dic = {}
        for i in x_list:
            n += 1
            if i in y_list:
                T+=1
                tt=y_list.index(i)
                del(y_list[tt])
            else:
                T+=0
                w_dic[n] = i
        if  T== len(x):
            print("is aAnagam")
            print(w_dic)
        else:
            print("is not Anaglam")
            print(w_dic)
    else:
        print("It is not Anagram because of length")


#str 형태로 리스트에 저장하려면 input().split()을, int 형태로 리스트에 저장하려면 list(map(int, input().split()))로
# a,b=input(("Enter two words").split(','))
a=input("1st")
b=input("2nd")

if type(a) and type(b) == str:
    isAnagram(a,b)

else:
    print("It is not Anagram because of input type")


