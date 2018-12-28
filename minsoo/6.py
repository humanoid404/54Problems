from datetime import datetime
age = 25
retire = 65
today = datetime.today().year
age = int(age)
retire = int(retire)
today  =int(today)
day = today + retire - age
[age, retire, today, day] = [str(age), str(retire), str(today), str(day)]
message = "What is your current age? " + age + "\n" + "At what age would you like to retire? " + retire + "\n" + "It's " + today + ", so you can retire in " + day + "."
print(message)