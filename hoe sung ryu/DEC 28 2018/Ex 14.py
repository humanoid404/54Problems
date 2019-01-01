# Excercise 14 <Tax calculator>

#    1)대문자는 가능 하게 받을 수 없나? -> upper/lower

# general
num = input("What is the order amount?")
state = input("what is the state?")
# rate_WI=5.5
# rate_MN=1
rate = {'WI': '5.5', 'MN': '1', 'CA': '1.3'}
state_dic = {'california': 'CA'}

if len(state) > 3:
    if state.lower() in state_dic.keys():
        abbri_state = state_dic[state.lower()]

else:
    abbri_state = state

Tax = float(rate[abbri_state]) * float(num)
Total_a = float(num) + tax
print('The total prices is %d' % Total_a, 'tax is %d' % Tax, sep='\n')