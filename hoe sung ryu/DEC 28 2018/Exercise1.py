#Excersice 1-1

def say_hello():
    print('what is your name')
    name=input()
    print('Hello , %s, nice to meet you!' %name)
# say_hellp()

#Excersice 1-2(challange)
def say_hello_different():
    name=input('what is your name')
    if name=='brain':
        print('Hello , %s, nice to meet you!' %name)
    elif name=='candy':
        print('Hi, %s, nice to see you again' %name)
    elif name=='hoesung':
        print('Master %s' %name)
    else:
        print('This is first we have met' %name)
    return

# say_hello_different()