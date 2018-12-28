def prompt(name):
    greetings = {"Kevin": "Hey, Kevin! Long time no see!!",
                 "James": "Greetings, milady!",
                 "Crook": "Who are you again?",
                 "Julia": "Begone, demon!"}
    if name in greetings:
        print("\n", greetings[name], sep="")
    else:
        print("\nHello, ", name, ", nice to meet you!", sep="")


if __name__ == "__main__":
    prompt(input("What is your name?\n"))
