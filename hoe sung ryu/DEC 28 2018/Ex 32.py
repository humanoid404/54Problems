'''Ex 32 Guess the number Game'''
import random as r
print("let's play guess the Number")
level=input("Pick a difficulty level 1,2,3")
while True:
    if level=='1':
        anw=r.randint(1,10)
        chance=3
        max_n=3
        while chance>0:
            chance-=1
            user_anw=input("What's your guess?")
            if anw == user_anw:
                if chance>=max_n-1:
                    print("You are a mind reader!")
                elif (max_n-3)<chance<(max_n-1):
                    print("Most impressive")
                elif (max_n-3)>=chance:
                    print("You can do better than that")
            break
            else:
                if 0<chance<3:
                    print("you have %d times left" %(4-chance))
                elif chance==max_n:
                    print("Beter luck next time")
                continue
    break
    elif level=='2':
        anw = r.randint(1, 100)
        chance = 3
        while chance > 0:
            chance -= 1
            user_anw = input("What's your guess?")
            if anw == user_anw:
                print("Collect")
                break
            else:
                continue
        break

    # elif level=='3':
    else:
        print("Please select level between 1 and 3")
        continue
