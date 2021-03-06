from random import random, randrange, shuffle
from numpy.random import geometric

specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_"]
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
numbers = list(map(str, range(10)))
elements = {"s": specialChars, "n": numbers, "a": vowels+consonants}
optionN = 3  # number of options


def genPW(minLength, specialCharN, numberN, prob=0.3):
    length = max(minLength, specialCharN+numberN)
    length += geometric(1/length)

    # randomized place holder of the element types: "a" for alphabet, "n" for number, "s" for special chars
    elemType = ["s"]*specialCharN + ["n"]*numberN + ["a"]*(length-specialCharN-numberN)
    shuffle(elemType)

    password = ""
    for i in range(length):
        character = elements[elemType[i]][randrange(len(elements[elemType[i]]))]
        if character in vowels and random() < prob:
            character = str(randrange(10))
        password += character
    return password


while __name__ == "__main__":
    try:
        minLength = int(input("What's the minimum minLength? "))
        if minLength <= 0:
            raise ValueError

        specialCharN = int(input("How many special characters? "))
        if specialCharN <= 0:
            raise ValueError

        numberN = int(input("How many numbers? "))
        if numberN <= 0:
            raise ValueError

        if optionN <= 1:
            print("Your password is {}\n".format(genPW(minLength, specialCharN, numberN)))
        else:
            print("Here are a few options for your password:")
            for i in range(1, 1+optionN):
                print("Option {}: {}".format(i, genPW(minLength, specialCharN, numberN)))
            print("")
    except ValueError:
        print("\nPlease enter a positive integer.")
