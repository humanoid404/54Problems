

#Exercise5-1
def simple_math(a,b,value):
    print('What is the first number? %d' %a)
    print('What is the second number? %d' %b)
    if value== '+':
        print('{0}+{1}= {2}'.format(a,b,a+b))
    elif value== '-':
        print('{0}-{1}= {2}'.format(a,b,a-b))
    elif value=='*':
        print('{0}*{1}= {2}'.format(a,b,a*b))
    elif value=='-':
        print('{0}/{1}= {2}'.format(a,b,a/b))
    elif value == None:
        print('insert logic symbol')
    else:
        print('insert valiable logic symbol')
#Exercise5-2
디따 어렵넹
