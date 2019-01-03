# prompt-dictionary binary tree
pdTree = ("Is the car alert when you turn the key? [Y/N]: ",
          {"Y": ("Are the battery terminals corroded? [Y/N]: ",
                 {"Y": ("Clean terminals and try starting again.",
                        {}),
                  "N": ("Replace cables and try again.",
                        {})}),
           "N": ("Does the car make a clicking noise? [Y/N]: ",
                 {"Y": ("Replace the battery.",
                        {}),
                  "N": ("Does the car crank up but fail to start? [Y/N]: ",
                        {"Y": ("Check spark plug connections.",
                               {}),
                         "N": ("Does the engine start and then die? [Y/N]: ",
                               {"Y": ("Does your car have fuel injuction? [Y/N]: ",
                                      {"Y": ("Get it in for service.",
                                             {}),
                                       "N": ("Check to ensure the choke is opening and closing.",
                                             {})}),
                                "N": ("Buy a new car.",
                                      {})})})})})


tree = pdTree  # subtree structure used for recursion
while tree[1]:  # loop until we hit an empty dictionary {}
    response = input(tree[0]).upper()
    if response not in tree[1]:
        currentKeys = sorted(tree[1].keys(), reverse=True)  # list of keys (possible inputs/branches) in the current position of the subtree in reverse order
        print("\nPlease enter either {}.".format(", ".join(currentKeys[:-1]) + " or " + currentKeys[-1]))
        continue
    else:
        tree = tree[1][response]
print(tree[0])
