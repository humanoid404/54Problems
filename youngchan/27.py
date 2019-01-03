from re import fullmatch


def validateFirstName(firstName):
    if not firstName:
        return "The first name must be filled in.\n"
    elif not fullmatch(r"[a-zA-Z]{2,}", firstName):
        return "\"{}\" is not a valid first name. The first name must be at least two characters long.\n".format(firstName)
    else:
        return ""


def validateLastName(lastName):
    if not lastName:
        return "The last name must be filled in.\n"
    elif not fullmatch(r"[a-zA-Z]{2,}", lastName):
        return "\"{}\" is not a valid last name. The last name must be at least two characters long.\n".format(lastName)
    else:
        return ""


def validateEmployeeID(employeeID):
    if not fullmatch(r"[a-zA-Z]{2}-\d{4}", employeeID):
        return "{} is not a valid ID. Enter two letters, a hyphen, and four numbers.\n".format(employeeID)
    else:
        return ""


def validateZipCode(zipCode):
    if not fullmatch(r"\d+", zipCode):
        return "The zip code must be numeric.\n"
    else:
        return ""


def validateInput(firstName, lastName, employeeID, zipCode):
    return validateFirstName(firstName) + validateLastName(lastName) + validateEmployeeID(employeeID) + validateZipCode(zipCode)


errors = "_"
while errors:
    firstName = input("Enter the first name: ")
    lastName = input("Enter the last name: ")
    employeeID = input("Enter an employee ID: ")
    zipCode = input("Enter the zip code: ")
    errors = validateInput(firstName, lastName, employeeID, zipCode)
    if errors: print(errors)

print("There were no errors found.\n")
