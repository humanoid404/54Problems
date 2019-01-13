'''Ex38 filtering Values'''



list= input('Enter a list of numbers, separated by spaces: ')

number=0
for i in list.split():
    i = int(i)

    if i%2==0:
        number+=i
        # number = number.join()

    else:
        pass



# while input() != '':
#     do_thing

a = input('Enter a list of numbers, separated by spaces: ')
number = ''
for x in a.split():
    try:
        x = int(x)
        if x % 2 == 0:
            number += f'{x}'
    except:
        pass

print(f"The even numbers are {number}")