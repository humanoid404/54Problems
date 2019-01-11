import json
import pandas as pd
import re
from string import capwords


def jsonDataToDataFrame(jsonData):
    data = {}
    for dic in jsonData['products']:
        for key in dic:
            if key not in data:
                data[key] = [dic[key]]
            else:
                data[key].append(dic[key])
    return pd.DataFrame(data)


def dataFrameToJsonData(dataFrame):
    rowNumber = dataFrame.shape[0]
    acc = []
    for n in range(rowNumber):
        temp = {}
        for k in dataFrame:
            temp[k] = dataFrame[k][n]
            if k == 'price':
                temp[k] = float(temp[k])  # convert type from numpy.float to float
            if k == 'quantity':
                temp[k] = int(temp[k])  # convert type from numpy.int to int
        acc.append(temp)
    return {"products": acc}


with open("44.data", "r") as f:
    jsonData = json.load(f)

df = jsonDataToDataFrame(jsonData)

while True:
    df_copy = df.copy().rename(columns=str.capitalize)
    df_copy["Price"] = df_copy["Price"].apply(lambda x: '${:,.2f}'.format(x))  # format the price in a new copy
    name = input("What is the product name? [regex]: ")
    if not name:
        break
    res = df_copy.loc[df_copy['Name'].str.contains(r"(?i)"+name)]
    if not res.empty:
        print(res)
        print('')
    else:
        print('Sorry, that product was not found in our inventiory.')
        while True:
            choice = input("Do you want to add the product? [Y/N]: ").upper().strip()
            if choice not in ["Y", "N"]:
                print("\nPlease enter either Y or N.")
                continue
            else:
                choice = choice == "Y"
                break
        if not choice:
            print('')
        else:
            name = capwords(name.lower())
            while True:
                inputPrice = input("Enter the price: ")
                if not re.fullmatch(r"( *\$* *)*(\d*\.(\d\d){0,1}|\d*)( *\$* *)*", inputPrice):
                    print("Invalid price.\n")
                    continue
                inputQuantity = input("Enter the quantity: ")
                if not re.fullmatch(r"\d*", inputQuantity):
                    print("Invalid quantity.\n")
                    continue
                if not inputPrice or not inputQuantity:
                    if not inputPrice and not inputQuantity:
                        print("Cancelling product addition.\n")
                        break
                    else:
                        print("Detected empty input. Restarting product addition.\n")
                        continue
                else:
                    inputdata = {"name": [name], "price": [float(inputPrice)], "quantity": [int(inputQuantity)]}
                    df = df.append(pd.DataFrame(inputdata), ignore_index=True)
                    jsonData = dataFrameToJsonData(df)
                    jsonString = json.dumps(jsonData, indent=4, sort_keys=True)
                    jsonString = re.sub(r'("price": \d+\.)(\d,)', '\g<1>0\g<2>', jsonString)
                    with open("44.data", "w") as f:
                        f.write(jsonString)
                    print("The product {} is added.\n".format(name))
                    break
