import re
import os


replaceMap = {}
with open("45.configCSV", "r") as confFile:
    confFile.readline()  # throw away the header "bad,good\n"
    for line in confFile:
        pair = line.strip('\n').split(",")  # the end of line contains \n
        if len(pair) == 2:
            replaceMap[pair[0]] = pair[1]


def replaceFile(readFileName, writeFileName):
    subCount = 0
    with open(readFileName, "r") as inFile:
        with open(writeFileName, "w") as outFile:
            for line in inFile:
                for k in replaceMap:
                    line, count = re.subn(r"(^|\W){}(\W|$)".format(k), r"\g<1>{}\g<2>".format(replaceMap[k]), line)
                    subCount += count
                outFile.write(line)
    print('Finished {} replacements from file "{}" written to file "{}".'.format(subCount, readFileName, writeFileName))




while True:
    option = input("[1]replace file, [2]replace files in directory\n[1/2]: ").strip().upper()
    if option not in ["1", "2"]:
        print("Invalid Input: Enter either 1 or 2.")
        continue
    else:
        multiple = option == "2"
        break

if not multiple:
    filename = input("What is the name of the output file? ")
    if not filename:
        filename = "filename"
        print('Default filename is "{}".'.format(filename))
    replaceFile("45.input", "45.output.{}".format(filename))
else:
    files = [f for f in os.listdir('./45.directory') if os.path.isfile(os.path.join('./45.directory', f))]
    if not files:
        print("There are no files to modify.")
    else:
        if os.path.exists("./45.directory/output") and not os.path.isdir("./45.directory/output"):
            print('Something named "45.directory/output" already exists.')
            print('Please delete or rename this and try again.')
        else:
            if not os.path.exists("./45.directory/output"):
                os.makedirs("./45.directory/output")
            for filename in files:
                replaceFile("./45.directory/{}".format(filename), "./45.directory/output/{}.replaced".format(filename))
