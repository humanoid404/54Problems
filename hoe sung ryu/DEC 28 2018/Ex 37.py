
'''string

string.ascii_lowercase contain small alphabet ex)abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase contain capital alphabet ex) ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters contain both small and large alphabet ex) abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.punctuation contain special symbol ex) !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~


'''
import random as r
import string


def passwordGenerator(length, special_ch, num):
    password = []
    for i in range(length - special_ch - num):
        password += r.choice(string.ascii_letters)
    for j in range(special_ch):
        password += r.choice(string.punctuation)
    for k in range(num + 1):
        password += r.choice(string.digits)
    r.shuffle(password)
    wpassword = ''.join(password)
    print(f"your password is {wpassword}.")


length = int(input("What is the minimum length?"))
special_ch = int(input("How many special characters?"))
num = int(input("How many numbers?"))

passwordGenerator(length, special_ch, num)





