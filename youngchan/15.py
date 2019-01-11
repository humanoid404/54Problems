from getpass import getpass

idpw = {"username": "password"}

id = input("What is the username?\n")
pw = getpass("What is the password?\n")

if id in idpw and pw == idpw[id]:
    print("Welcome!")
else:
    print("I don't know you.")
