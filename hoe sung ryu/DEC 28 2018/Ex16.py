# ex 16
age = int(input("what is your age"))
state = {0: 'you are not', 1: 'you can'}
if age > 18:
    judge = 0
else:
    judge = 1

print(state[judge])