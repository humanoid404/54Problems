months = {"1": "January",
          "2": "February",
          "3": "March",
          "4": "April",
          "5": "May",
          "6": "June",
          "7": "July",
          "8": "August",
          "9": "September",
          "10": "October",
          "11": "November",
          "12": "December"}

while True:
    try:
        m = input("Please enter the number of the month: ")
        if m not in months:
            raise ValueError
        else:
            print("The name of the month is {}.\n".format(months[m]))
    except ValueError:
        print("\nPlease enter an integer between 1 and 12")
