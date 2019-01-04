# Ex 28 fail
list = [1, 2, 3]
print(len(list))
print(list[0])
print(list[1])
print(list[2])

n = input("How many number ")
while n > 0:
    n = n - 1
    input("Enter a number: ")

list = []
for i in range(len(list)):
    S = 0
    S = S + list[i]

print(S)