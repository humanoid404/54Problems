tax = 0.055
c = 1-tax
p1 = 25
q1 = 2
p2 = 10
q2 = 1
p3 = 4
q3 = 1
[p1, p2, p3, q1, q2, q3] = [float(p1), float(p2), float(p3), int(q1), int(q2), int(q3)]
subtotal = p1*q1 + p2*q2 + p3*q3
Tax = subtotal*tax
Total = c*subtotal
print('Price of item 1: ', p1)
print('Quantity of item 1: ', p1)
print('Price of item 1: ', p2)
print('Quantity of item 1: ', p2)
print('Price of item 1: ', p3)
print('Quantity of item 1: ', p3)
print('Tax: $', Tax)
print('Subtotal: $', subtotal)
print('Total: $', Total)