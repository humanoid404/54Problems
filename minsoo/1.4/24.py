print("Enter two strings and I'll tell you if they are anagrams: ")
def isAnagram(a,b):
    if len(a) == len(b):
        A = ''
        for i in range(len(a)):
            for j in range(len(b)):
                try:
                    if a[i] == b[j]:
                        A = A + a[i]
                except:
                    pass
        print(A)
        print(a)
        if len(A) == len(C):
            result = ''
        else:
            result = 'not '
    else:
        result = 'not '
    print(f'"{a}" and "{b}" are {result}anagrams')
a = input('Enter the first string: ')
b = input('Enter the second string: ')
isAnagram(a, b)
