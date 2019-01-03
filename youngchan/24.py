def isAnagram(word1, word2):
    isAnagramFlag = True
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[-1-i]:
                isAnagramFlag = False
    else:
        isAnagramFlag = False
    return isAnagramFlag


print("Enter two strings and I'll tell you if they are anagrams.")
word1 = input("Enter the first string: ").strip()
word2 = input("Enter the second string: ").strip()
print("\"{}\" and \"{}\" are {}anagrams.".format(word1, word2,
                                                 "" if isAnagram(word1, word2) else "not "))
