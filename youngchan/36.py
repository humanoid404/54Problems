from numpy import mean, std

acc = []
while True:
    try:
        time = input("Enter a number: ")
        if time == "done":
            break
        acc.append(int(time))
    except ValueError:
        print('Enter a number, or enter "done" to termiate.')

print("\nNumbers: ", ", ".join(map(str, acc)))
print("The average is {:.2f}".format(mean(acc)))
print("The minimum is {}".format(min(acc)))
print("The maximum is {}".format(max(acc)))
print("The standard deviation is {:.2f}".format(std(acc)))
