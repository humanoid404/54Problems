import re
import os

while True:
    name = input("Site name: ")
    if not re.fullmatch(r"\w+", name):
        print('\nSite name "{}"" is invalid'.format(name))
        continue
    elif os.path.isdir("./43.directoy/{}".format(name)):
        print('\nThe directory "./43.directoy/{}" already exists!'.format(name))
        continue
    else:
        break

author = input("Author: ")

while True:
    folderJS = input("Do you want a folder for JavaScript? [Y/N]: ").upper().strip()
    if folderJS not in ["Y", "N"]:
        print("Please enter either Y or N.")
        continue
    else:
        folderJS = folderJS == "Y"
        break

while True:
    folderCSS = input("Do you want a folder for CSS? [Y/N]: ").upper().strip()
    if folderCSS not in ["Y", "N"]:
        print("Please enter either Y or N.")
        continue
    else:
        folderCSS = folderCSS == "Y"
        break


os.makedirs("./43.directoy/{}".format(name))
print("Created ./43.directoy/{}".format(name))
with open("./43.directoy/{}/index.html".format(name), "w") as f:
    f.write(
"""
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="author" content="John Doe">

  <title>Page Title</title>
</head>

<body>
</body>

</html>
"""
)
print("Created ./43.directoy/{}/index.html".format(name))
if folderJS:
    os.makedirs("./43.directoy/{}/js".format(name))
    print("Created ./43.directoy/{}/js".format(name))
if folderCSS:
    os.makedirs("./43.directoy/{}/css".format(name))
    print("Created ./43.directoy/{}/css".format(name))
