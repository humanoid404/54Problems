import json
from pprint import pprint

json_data = open('C:/Users/wwnis/Desktop/44.JSON').read()
data = json.loads(json_data)
pprint(data)
a = 0
while a != True:
    a = input('What is the product name? ')
    for i in range(len(data["products"])):
        if data["products"][i]["name"] == a:
            a = True
            print(f'Name: {data["products"][i]["name"]}')
            print(f'Price: ${data["products"][i]["price"]}')
            print(f'Quantity on hand: {data["products"][i]["quantity"]}')
            break
    if a != True: print('Sorry, that product was not found in our inventory.')
