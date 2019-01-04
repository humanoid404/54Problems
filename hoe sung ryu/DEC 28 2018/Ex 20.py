
#<Exercise 20>

#1.general

amount=float(input("What is the order amount?"))
user_state=input("Where do you live?").lower()

diff_rate_state=['wisconsin','CA']

# if there exist sub-country then print sub-country list
if user_state in diff_rate_state:
    user_country=input("Where is your country?").lower()
    user_country=user_country.replace(" ", "") #delete the blank
else:
    pass # just pass literally

#representation of tax rate
tax_rate={'wisconsin': 'wisconsin_country', "illinois":0.08}
wisconsin_country={'eauclaire':0.005,'dunncountry':0.004}

#If tax_rate is not numeric then go to the country dic and find value

if  type(tax_rate.get(user_state)) == str:
    rate=wisconsin_country.get(user_country)
else:
    rate=tax_rate.get(user_state)

amount_tax=round(amount*rate,2)
t_amount=round(amount+amount_tax,2)

print("The tax is $ %s." %amount_tax,"The total is $ %d." %t_amount,sep='\n')
#additing country
#어찌 중첩 됬다는 거지 ???????  implement the program using data structures to avoid nested if state


#2.challenges
amount=float(input("What is the order amount?"))
user_state=input("Where do you live?").lower()

tax_rate={'wisconsin': 'wisconsin', "illinois":0.08} #representation of tax rate
wisconsin={'eauclaire':0.005,'dunncountry':0.004}
diff_rate_state=['wisconsin','CA']

# if there exist sub-country then print sub-country list
if user_state in diff_rate_state:
    user_country=input("Where is your country?").lower()
    user_country=user_country.replace(" ", "") #delete the blank
    #if user_country is not exist in user_state, then add
    if user_country in eval(user_state):
        pass
    else:
        add_country_tax=float(input("Your country tax data does not exist. So input tax rate of {country}".format(country=user_country)))
        eval(user_state)[user_country]=add_country_tax
#         d[user_country]=add_country_tax
else:
    pass # just pass literally


#If tax_rate is not numeric then go to the country dic and find value

if  type(tax_rate.get(user_state)) == str:
    rate=wisconsin.get(user_country)
else:
    rate=tax_rate.get(user_state)

amount_tax=round(amount*rate,2)
t_amount=round(amount+amount_tax,2)

print("The tax is $ {dollar} .".format(dollar=amount_tax),"The total is $ {dollar}.".format(dollar=t_amount),sep='\n')