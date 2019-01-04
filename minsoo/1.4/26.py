import math
def calculateMonthsUntilPaidOff(b,i,p):
    b, i, p = float(b), float(i), float(p)
    n = math.ceil((math.log(1+(b/round(p,2))*(1+(1+0.01*i)**30)))/(math.log(1+0.01*i))) # 공식이 좀 이상한듯
    return n

print(f"It will take you {calculateMonthsUntilPaidOff(input('What is your balance? '), input('What is the APR on the card (as a percent)? '), input('What is the monthly payment you can make? '))} months to pay off this card.")