def filterEvenNumbers(numbers):
    acc = []
    for n in numbers:
        if n%2==0:
            acc.append(n)
    return acc


while __name__ == "__main__":
    try:
        inputs = input("Enter a list of integers separated by spaces: ").split(" ")
        numbers = []
        for i in inputs:
            numbers.append(int(i))
        numbers = [str(n) for n in filterEvenNumbers(numbers)]
        print("The even numbers are {}.".format(" ".join(numbers)))
    except ValueError:
        print("\nPlease enter a valid input.")
