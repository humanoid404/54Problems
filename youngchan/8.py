import re

patternNonnegativeInteger = re.compile(r"\d+")


flag1 = True

if flag1:
    while True:
        people = input("How many people?\n")
        if not re.fullmatch(patternNonnegativeInteger, people):
            print("\nPlease input a nonnegative integer.")
        else:
            people = int(people)
            break

    while True:
        pizzas = input("How many pizzas do you have?\n")
        if not re.fullmatch(patternNonnegativeInteger, pizzas):
            print("\nPlease input a nonnegative integer.")
        else:
            pizzas = int(pizzas)
            break

    while True:
        piecesPerPizza = input("How many pieces does each pizza have?\n")
        if not re.fullmatch(patternNonnegativeInteger, piecesPerPizza):
            print("\nPlease input a nonnegative integer.")
        else:
            piecesPerPizza = int(piecesPerPizza)
            break

    print("\n{} {} {} {} pizza{} each of {} piece{}".format(people if people > 0 else "no",
                                                            "people" if people != 1 else "person",
                                                            "with" if people > 0 else "and",
                                                            pizzas if pizzas > 0 else "no",
                                                            "s" if pizzas > 1 else "",
                                                            piecesPerPizza,
                                                            "s" if piecesPerPizza != 1 else ""))

    if people == 0:
        if pizzas > 0:
            print("There is nobody to share :(\n")
        else:
            print("How depressing :(\n")
    else:
        q = (pizzas*piecesPerPizza) // people  # each person gets q pieces of pizza
        r = (pizzas*piecesPerPizza) % people  # there are r leftover pieces of pizza
        print("Each person gets {} piece{} of pizza.".format(q if q > 0 else "no",
                                                             "s" if q > 1 else ""))
        print("There {} {} leftover piece{}.".format("are" if r != 1 else "is",
                                                         r if r > 0 else "no",
                                                         "s" if r != 1 else ""))

###############################################################################


flag2 = True

if flag2:
    while True:
        people = input("\nHow many people?\n")
        if not re.fullmatch(patternNonnegativeInteger, people):
            print("\nPlease input a nonnegative integer.")
        else:
            people = int(people)
            if people == 0:
                print("You don't need any pizza!\n")
            else:
                break

    while True:
        piecesPerPizza = input("How many pieces does each pizza have?\n")
        if not re.fullmatch(patternNonnegativeInteger, piecesPerPizza):
            print("\nPlease input a nonnegative integer.")
        else:
            piecesPerPizza = int(piecesPerPizza)
            if piecesPerPizza == 0:
                print("Each pizza needs at least one piece!\n")
            else:
                break

    pizzasPieceAcc = 0
    for i in range(1, 1+people):
        while True:
            ithPieceNumber = input("How many pieces of pizza does the person number {} out of {} want?\n".format(i, people))
            if not re.fullmatch(patternNonnegativeInteger, ithPieceNumber):
                print("\nPlease input a nonnegative integer.")
            else:
                ithPieceNumber = int(ithPieceNumber)
                break
        pizzasPieceAcc += ithPieceNumber

    pizzas = pizzasPieceAcc // piecesPerPizza
    if pizzasPieceAcc % piecesPerPizza > 0:
        pizzas += 1

    print("\n{} {} want{} {} piece{} of pizza each of {} piece{}.".format(people if people > 0 else "no",
                                                       "people" if people > 1 else "person",
                                                       "" if people > 1 else "s",
                                                       pizzasPieceAcc if pizzasPieceAcc > 0 else "no",
                                                       "" if pizzasPieceAcc > 1 else "s",
                                                       piecesPerPizza,
                                                       "s" if piecesPerPizza != 1 else ""))
    print("You need {} pizza{}.".format(pizzas if pizzas > 0 else "no",
                                       "s" if pizzas > 1 else ""))
