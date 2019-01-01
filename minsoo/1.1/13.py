P = float(input('What is the principal amount?'))
r = float(input('What is the rate? ( %)'))
t = float(input('What is the number of years?'))
n = float(input('What is the number of times the interest is compounded per year: '))

A = P*(1+r/(100*n))**(n*t)
print('${} invested at {}% for {} years compounded {} times per year is ${}'.format(P, r, t, n, A))