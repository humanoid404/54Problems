print("Enter two strings and I'll tell you if they are anagrams: ")
def isAnagram(a,b):
    if len(f'{a}') == len(f'{b}'):
        result = ''
    else:
        result = 'not '
    print(f'"{a}" and "{b}" are {result}anagrams')
isAnagram(input('Enter the first string: '), input('Enter the second string: '))