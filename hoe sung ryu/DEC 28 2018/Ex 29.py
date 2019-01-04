#Handling Bad Input


def rule(r):
    while True:
        r= input("What is the rate of return?")
        if type(eval(r))==int:
            r=int(r)
            years=72/r
            print("It will take {years} years to double your initial investment".format(years=round(years)))
            break
        elif r==0:
            print("Rate can not be zero")
        else:
            print("That's not a valid input", '\n' ,"Input must be numeric")


rule(r)



