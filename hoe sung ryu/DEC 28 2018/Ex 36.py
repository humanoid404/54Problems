'''Ex 36 Comp[uting Statistics'''


def mean(x):
    sum=0
    for i in range(len(x)):
        sum=sum+x[i]
    mean=sum/len(x)
    return mean

def var(x):
    sum=0
    x_2 = list(map(lambda x: x ** 2, x))
    for i in range(len(x)):
        sum=sum+x[i]
    x_2_mean=sum/len(x)
    var=x_2_mean-(mean(x))**2
    return var

def standar_deviation(x):
    stdv=var(x)**(1/2)
    return stdv

t=''
element=[]
while t.lower!='done':
    t=str(input("Enter a number: "))
    element.append(t)
    if t.lower=='done':
        mean(element)
        var(element)
        standar_deviation(element)
        print(mean,var,stdv)
        break
    else:
        continue


