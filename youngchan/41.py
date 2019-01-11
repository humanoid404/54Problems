from pathlib import Path

while True:
    option = input("[1]Sort file, [2]Sort user input.\n[1/2]: ").strip()
    if option not in ["1", "2"]:
        print("\nPlease enter either 1 or 2.")
        continue
    elif option == "1":
        filename = input("Enter the file name to sort: ")
        if Path(filename).is_file():
            with open(filename, "r") as file:
                lines = file.read().split("\n")
                lines = list(filter(lambda x: x, map(lambda x: x.strip(), lines)))
                lines.sort()
            with open("41.write", "w") as writefile:
                for l in lines:
                    writefile.write(l+"\n")
            print('\nThe sorted file of "{0}" is written as "41.write".'.format(filename))
        else:
            print('\nThe file "{}" does not exist or is not readable.'.format(filename))
            continue
    else:
        print("Enter the lines to sort.")
        print('The sorted input will be written in the file "41.write".')
        print('Enter a blank line to end input.')
        acc = []
        while True:
            userInput = input('')
            if not userInput:
                break
            acc.append(userInput)
        acc.sort()
        with open("41.write", "w") as writefile:
            for l in acc:
                writefile.write(l+"\n")
        print('The sorted input is written in the file "41.write".')
