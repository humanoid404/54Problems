from random import randrange

contestants = []
while True:
    name = input("Enter a name: ")
    if name:
        contestants.append(name)
    else:
        break
while contestants:
    try:
        number = int(input("How many winners will you choose? "))
        if number <= 0:
            break
        for i in range(min(number, len(contestants))):
            winner = contestants[randrange(len(contestants))]
            print("The winner is... {}.".format(winner))
            contestants.remove(winner)
    except ValueError:
        print("\nPlease enter a valid number.")
