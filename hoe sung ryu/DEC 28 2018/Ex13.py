# Excercise 13 <Determining Compound Interest>

#general
P=float(input("principal"))
r=float(input("rate of interest"))
r_p=r*0.01
t=float(input("the number of years"))
n=float(input("the number of times the interest is compunded per year"))

formula=P*(1+r_p/n)**(n*t)
ans=round(formula-P)
print("${0} invested at {1}% for {2}years compunded {3}"
      .format(int(P),r,int(t),int(n)+
      "times per year is $%s" %ans)