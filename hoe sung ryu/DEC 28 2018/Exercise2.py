#Excersice 2-1

def count_string():
    string=input('what is the input string?')
    num=len(string)
    print('{0} has {1} characters.'.format(string, num))
# count_string()


#Exercice 2-2
def count_string_nothing():
    string=input('what is the input string?')
    while True:
        count_string()


# count_string_nothing()