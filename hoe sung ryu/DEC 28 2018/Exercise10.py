
tax_rate=0.055
subtotal=1000
Tax=str(tax_rate*subtotal)
Total=str((1+tax_rate)*subtotal)
#input('Are you sure? is there anything stuff buy more?')
print('Tax: '+'$'+Tax,'Total: 
      '+'$'+Total,sep='\n')


item1_name=input('What did you buy?')
item1_number=input('Enter the quantity of %s' %item1_name)
try:
    if type(item1_number)== int and int(item1_number)>0:
    item1=input('Enter the each price of %s' %item1_name)
total_item1=int(item1_number)*int(item1)
total_tax_item1=0.55*total_item1
print('total_item1 %d'%total_item1,'tax %d'%total_tax_item1,sep='\n')


def accept_fct(a):
      while True:
            try:
                  if int(a) >= 0:
                        a = int(a)
                        print('yes')
                        break
                  else:
                        print('{0} must be positive int'.format(a))
                        a = input()
                        continue
            except:
                  print('{0} must be positive int'.format(a))
                  a = input()
                  continue
