#Ex 12

#computing simple interest
P=float(input("principal"))
r=float(input("rate of interest"))
t=float(input("the number of years"))
r_p=r*0.01
formula=P*(1+r_p*t)
ans=round(formula-P)
print("After {0} at {1}%, the investment will be worth ${2}"
      .format(int(t),r,ans))