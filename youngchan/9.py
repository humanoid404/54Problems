import re
from math import pi, ceil


def promptShape():
    while True:
        shape = input("Choose the shape of your room: [1] Square, [2] Hemisphere, [3] L\n")
        if not re.fullmatch(patternShape, shape):
            print("\nPlease input either 1, 2 or 3.")
        else:
            return int(shape)


def promptSquare():
    while True:
        length = input("What is the length of the room in feet?\n")
        if not re.fullmatch(patternNumber, length):
            print("\nPlease enter a valid number.")
        else:
            length = float(length)
            break

    while True:
        width = input("What is the width of the room in feet?\n")
        if not re.fullmatch(patternNumber, width):
            print("\nPlease enter a valid number.")
        else:
            width = float(width)
            break
    return length, width


def promptHemisphere():
    while True:
        radius = input("What is the radius of the room in feet?\n")
        if not re.fullmatch(patternNumber, radius):
            print("\nPlease enter a valid number.")
        else:
            return float(radius)


def promptL():
    while True:
        length1 = input("What is the maximum vertical length of the whole room in feet?\n")
        if not re.fullmatch(patternNumber, length1):
            print("\nPlease enter a valid number.")
        else:
            length1 = float(length1)
            break

    while True:
        length2 = input("What is the maximum horizontal length of the whole room in feet?\n")
        if not re.fullmatch(patternNumber, length2):
            print("\nPlease enter a valid number.")
        else:
            length2 = float(length2)
            break

    while True:
        width1 = input("What is the width of the vertical part of the room in feet?\n")
        if not re.fullmatch(patternNumber, width1):
            print("\nPlease enter a valid number.")
        else:
            width1 = float(width1)
            if width1 > length2:
                print("Something is wrong. This width must be smaller than {}. Try Again.".format(length2))
            else:
                break

    while True:
        width2 = input("What is the width of the horizontal part of the room in feet?\n")
        if not re.fullmatch(patternNumber, width2):
            print("\nPlease enter a valid number.")
        else:
            width2 = float(width2)
            if width2 > length1:
                print("Something is wrong. This width must be smaller than {}. Try Again.".format(length1))
            else:
                break

    return length1, width1, length2, width2


def calcSquare(length, width):
    coverSquareFeet = length*width
    purchaceGallons = ceil(coverSquareFeet / k)
    return purchaceGallons, coverSquareFeet


def calcHemisphere(radius):
    coverSquareFeet = 2*pi*radius**2
    purchaceGallons = ceil(coverSquareFeet / k)
    return purchaceGallons, coverSquareFeet


def calcL(length1, width1, length2, width2):
    coverSquareFeet = length1*width1 + length2*width2 - width1*width2
    purchaceGallons = ceil(coverSquareFeet / k)
    return purchaceGallons, coverSquareFeet


def promptResult(purchaceGallons, coverSquareFeet):
    print("\nYou will need to purchace {} gallons of paint to cover {} square feet.".format(purchaceGallons, round(coverSquareFeet, 5)))


if __name__ == "__main__":
    patternNumber = re.compile(r"\d+(\.\d+)?")
    patternShape = re.compile(r" *0*[123] *")
    k = 350  # 1 gallons cover 350 square feet

    shape = promptShape()
    if shape == 1:  # square shape
        promptResult(*calcSquare(*promptSquare()))
    elif shape == 2:  # hemisphere shape
        promptResult(*calcHemisphere(promptHemisphere()))
    else:  # shape == 3: "L" shape
        promptResult(*calcL(*promptL()))
