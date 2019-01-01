# Exercise 11 Currency conversion

def Currency_conversion():
    rate = {'USA': '1.00', 'KOR': '1', 'Japan': '1.03'}
    print(list(rate.keys()))
    cur = input("which currency do you have? choose above options")
    ex_cur = input("Which currency do yo want to exchange? choose above options")
    quan = float(input("How much do you want to exchange"))
    cur_value = float(rate.get(cur))
    ex_cur_value = float(rate.get(ex_cur))
    formula_cur = quan * cur_value / ex_cur_value
    amount = quan * formula_cur
    print("{0} {1} at an exchange rate of {2} is {3} {4}."
          .format(quan, cur, cur_value, amount, ex_cur))


#     while True:
#         cur=input("which currency do you have? choose above options")
#         ex_cur=input("Which currency do yo want to exchange? choose above options")
#         quan=float(input("How much do you want to exchange"))
#         if eval(cur) and eval(ex_cur) is str:
#             cur_value=float(rate.get(cur))
#             ex_cur_value=float(rate.get(ex_cur))
#             formula_cur= quan*cur_value/ex_cur_value
#             amount= quan * formula_cur
#             print("{0} {1} at an exchange rate of {2} is {3} {4}."
#                      .format(quan, cur,cur_value,amount,ex_cur))
#             break
#         else:
#              print("input must be int or float")
#              continue

Currency_conversion()  