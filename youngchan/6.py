import re
from datetime import datetime

pattern = re.compile(r"^[1-9]\d{0,2}$")

while True:
    age = input("What is your curent age?\n")
    if re.match(pattern, age):
        age = int(age)
        break
    else:
        print("\nPlease input a valid age.")

while True:
    retireAge = input("At what age would you like to retire?\n")
    if re.match(pattern, retireAge):
        retireAge = int(retireAge)
        break
    else:
        print("\nPlease input a valid age.")

currentYear = (datetime.now()).year

remainingYears = retireAge-age

if remainingYears > 0:
    print("\nYou have {0} years left until you can retire.".format(remainingYears))
    print("It's {0}, so you can retire in {1}.".format(currentYear, currentYear+remainingYears))
else:
    print("\nYou can already retire!")
