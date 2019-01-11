import pandas as pd
from datetime import date, datetime as dt
from dateutil.relativedelta import relativedelta


df = pd.DataFrame({
        'First Name': ['John', 'Tou', 'Michaela', 'Jake', 'Jacquelyn', 'Sally'],
        'Last Name': ['Johnson', 'Xiong', 'Michaelson', 'Jacobson', 'Jackson', 'Weber'],
        'Position': ['Manager', 'Software Engineer', 'District Manager', 'Programmer', 'DBA', 'Web Developer'],
        'Separation Date': [dt(2016, 12, 31), dt(2016, 10, 5), dt(2015, 12, 19), None, None, dt(2015, 12, 18)]
})


def searchByName(df):
    name = input("Enter a search string: ").strip()
    return df.loc[df['First Name'].str.contains(r"(?i)"+name) | df['Last Name'].str.contains(r"(?i)"+name)]


def searchByPosition(df):
    pos = input("Enter a search string: ").strip()
    return df.loc[df['Position'].str.contains(r"(?i)"+pos)]


def searchMonthsAgo(df, months=-6):
    monthsAgo = date.today()+relativedelta(months=months)
    return df.loc[df['Separation Date'] <= dt(monthsAgo.year, monthsAgo.month, monthsAgo.day)]


searching = {"1": searchByName,
             "2": searchByPosition,
             "3": searchMonthsAgo}


while __name__ == "__main__":
    print("You may search by [1]name, [2]position, or [3]find everybody whose separation date is six months ago or more.")
    searchBy = input("Search by [1/2/3]: ").strip()
    if searchBy not in ["1", "2", "3"]:
        print("\nPlease enter either 1, 2 or 3")
        continue
    else:
        print(searching[searchBy](df))
        print("")
