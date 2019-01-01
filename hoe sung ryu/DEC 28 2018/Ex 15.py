#Ex 15
#general
a=0
while a<5:
    password=input("What is the password ")
    if password == 1234:
        print("welcome")
        break
    else:
        a=a+1
        if a<5 and a>0:
            print("wrong","you have %d times left"%(5-a))
        elif a==5:
            print("your data has been removed")