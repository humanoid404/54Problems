from random import randrange, shuffle

prompts = ["Yes", "No", "Maybe", "Ask again later."]

while True:
    ques = input("What is your question?\n")
    if ques in ["shake", "shuffle"]:
        shuffle(prompts)
    else:
        print(prompts[randrange(0, len(prompts))])
