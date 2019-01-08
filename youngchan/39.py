import pandas as pd
from datetime import datetime as dt

df = pd.DataFrame({
        'First Name': ['John', 'Tou', 'Michaela', 'Jake', 'Jacquelyn'],
        'Last Name': ['Johnson', 'Xiong', 'Michaelson', 'Jacobson', 'Jackson'],
        'Position': ['Manager', 'Software Engineer', 'District Manager', 'Programmer', 'DBA'],
        'Separation date': [dt(2016, 12, 31), dt(2016, 10, 5), dt(2015, 12, 19), None, None]
})

while __name__ == "__main__":
    print("You may sort by '" + "', '".join([k for k in df]) + "'")
    sortBy = input("Sort by: ")
    if sortBy not in df:
        print("\nYou can't sort by {}".format(sortBy))
        continue
    print(df.sort_values(sortBy))
    print("")
