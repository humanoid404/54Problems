import pandas as pd

df = pd.read_csv("42.data", names=["Last", "First", "Salary"])
df_new = df.sort_values("Salary")
df_new["Salary"] = df_new["Salary"].apply(lambda x: '${:,.2f}'.format(x))
print(df_new)
