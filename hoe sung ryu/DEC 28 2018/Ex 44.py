

# Making JSON file input:json.dump , output:json.dumps
def make_JSON(x,y):
    name=str(x+'.json')
    with open(name, 'w', encoding="utf-8") as make_file:
        json.dump(y, make_file, ensure_ascii=False, indent="\t") #indent="\t" 옵션을 줘서 탭 문자로 들여쓰기를 함으로써 가독성을 향상시킵니다.)

#adding product
def add_product(x):
    new_product={}
    pro_name=input("What is the product name?")
    pro_price=input("What is the product price?")
    pro_quantity=input("What is the product quantity?")
    new_product["name"]=pro_name
    new_product["price"]=pro_price
    new_product["quantity"]=pro_quantity
    return x.append(new_product)

import json
from collections import OrderedDict #알파펫순서로 자동정렬 방지

# Ready for initial data
products_data = OrderedDict()
products_data["products"] = [{"name": "Widget", "price": "25.00", "quantity": "5"},
                             {"name": "Thing", "price": "15.00", "quantity": "5"},
                             ]

#make JSON
# make_JSON('products_data',products_data)

# Print JSON
# print(json.dumps(products_data, ensure_ascii=False, indent="\t"))


#read json file
with open('products.json', 'rb') as f:
  root = json.load(f)

product_list=root['products']
# product_list=[{"name": "Widget", "price": "25.00", "quantity": "5"},
#                              {"name": "Thing", "price": "15.00", "quantity": "5"},
#                              ]

a = True
while a:
    search = input("What is the product name?")
    for i in range(len(product_list)):
        if search == product_list[i]['name']:
            print(f"Name: {product_list[i]['name']}")
            print(f"Price: ${product_list[i]['price']}")
            print(f"Quantity on hand: {product_list[i]['quantity']}")
            a = False
            break
        print("Sorry, that product was not found in our inventory.")
        break

anw=input("Do you want add other item? Y/N")

if anw.lower()=='y':
    add_product(product_list)
    products_data["products"]=product_list
    #Save file
    make_JSON('products_data',products_data)
    # re-open JSON file for confirming
    with open('products_data.json', 'rb') as f:
        root = json.load(f)
    product_list = root['products']
    print(product_list)
else:
    pass




