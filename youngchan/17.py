while True:
        try:
            prompts = ["What is your weight in pounds?\n",
                       "What is your gender? [M/F]\n",
                       "How many drinks did you take?\n",
                       "What is the volume, in ounces, of alcohol per the drinks consumed?\n",
                       "How many hours has it passed since your last drink?\n"]
            w, g, n, v, h = map(input, prompts)
            g = (g.strip()[0]).upper()
            if g not in ["M", "F"]: raise ValueError
            n = int(n)
            w, v, h = map(float, [w, v, h])
            r = 0.73 if g == "M" else 0.66
            bac = (n*v*5.14/(w*r))-0.15*h
            print("\nYour BAC is {}".format(bac))
            print("It is {}legal for you to drive.\n".format("" if bac < 0.08 else "not "))
        except ValueError:
            print("Please enter a valid number or value.\n")
