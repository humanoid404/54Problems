# -1=different length, 0=same length not anagram, 1=anagram
def isAnagram(word1, word2):
    word1 = word1.lower().strip()
    word2 = word2.lower().strip()
    if len(word1) != len(word2):
        return -1
    l = len(word1)  # word length

    d = {}  # dictionary for recording the index per word
    # d=={"c":[[1,3], [2,4]], ...} will mean that "c" appears at the 1st, 3rd index in word1
    #                                         and "c" appears at the 2nd, 4th index in word2
    for i1 in range(l):
        if word1[i1] not in d:
            d[word1[i1]] = [[i1],[]]
        else:
            d[word1[i1]][0].append(i1)
    for i2 in range(l):
        if word2[i2] not in d:
            d[word2[i2]] = [[],[i2]]
        else:
            d[word2[i2]][1].append(i2)
    for k in d:
        if len(d[k][0]) != len(d[k][1]):
            return 0
    return 1


while True:
    print("Enter two strings and I'll tell you if they are anagrams.")
    word1 = input("Enter the first string: ")
    word2 = input("Enter the second string: ")
    isAnagramFlag = isAnagram(word1, word2)
    if isAnagramFlag < 0:
        print('"{}" and "{}" are not anagrams because they have different lengths.\n'.format(word1, word2))
    elif isAnagramFlag == 0:
        print('"{}" and "{}" are not anagrams.\n'.format(word1, word2))
    else:
        print('"{}" and "{}" are anagrams.\n'.format(word1, word2))
