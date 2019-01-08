from random import randint


def promptLevel(maxLevel):
    if maxLevel <= 0:
        return 0
    while True:
        try:
            level = int(input("Difficulty Level [{}]: ".format("/".join(map(str, range(1, 1+maxLevel)))
                                                               if maxLevel <= 5
                                                               else "1/.../"+str(maxLevel))))
            if 1 <= level <= maxLevel:
                return level
            print("\nPlease enter a number between 1 and ", maxLevel)
        except ValueError:
            print("\nPlease enter a valid number.")


def promptGame(level):
    number = randint(1, 10**level)
    guesses = []
    while True:
        try:
            if not guesses:
                guesses.append(int(input("I have my number. What's your guess? ")))
            else:
                guesses.append(int(input("Guess again: ")))

            if guesses[-1] in guesses[:-1]:
                print("You already guessed that number! ", end='')
            elif guesses[-1] < number:
                print("Too low. ", end='')
            elif guesses[-1] > number:
                print("Too high. ", end='')
            else:
                print("You got it in {} guesses!".format(len(guesses)))
                return level, len(guesses)
        except ValueError:
            guesses.append(False)
            print("That's not a number! ", end='')


def promptComment(level, numberOfGuesses):
    comments = {range(1, 1+level): "You're a mind reader!",
                range(1+level, 1+3*level): "Most impressive.",
                range(1+3*level, 1+6*level): "You can do better "}
    inRange = list(filter(lambda key: numberOfGuesses in key, comments.keys()))
    if not inRange:
        print("Better luck next time.")
    else:
        print(comments[inRange[0]])


def promptReplay():
    while True:
        replay = input("Play again? [Y/N]: ").strip().upper()
        if replay in ["Y", "YES"]:
            return True
        elif replay in ["N", "NO"]:
            return False
        else:
            print("\nPlease enter either Y or N.")


def playGame(maxLevel):
    while True:
        promptComment(*promptGame(promptLevel(maxLevel)))
        if not promptReplay():
            break


if __name__ == "__main__":
    maxLevel = 3
    playGame(maxLevel)
