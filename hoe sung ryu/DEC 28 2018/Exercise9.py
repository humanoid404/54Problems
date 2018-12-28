


area=input('What is the area of the room?')
while True:
    try:
        if int(area)>0:
            area=int(area)
            if area%350==0:
                num=area//350
            else:
                num=(area//350)+1
            print('You will need to purchase {0} gallons of paint to cover {1} square feet.'.format(area,num))
            break
        else:
            print('input must be positive int')
            area=input('What is the area of the room?')
            continue
    except:
        print('input must be positive int')
        area=input('What is the area of the room?')
        continue