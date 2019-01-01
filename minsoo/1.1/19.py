D = {'FT':12, 'FEET': 12, 'CM': 0.39, 'IN':1, 'INCH':1, 'IN.':1, 'KG':2.2, 'KILOGRAM':2.2, 'LB':1, 'POUND':1, 'LBS':1}

w_unit = input('Select unit of weight: kg, lb ')
w_float = input('Enter your weight')
h_unit = input('Select unit of height: ft, cm, in. ')
h_float = input('Enter your height')


while 1:
    if w_unit.upper() in D and h_unit.upper() in D:
        while 1:
            if [type(w_float), type(h_float)] != [float, float]:
                try:
                    w_float = float(w_float)
                    h_float = float(h_float)
                except:
                    print('Enter the numeric values of your weight and height')
                    w_float = input('Enter your weight')
                    h_float = input('Enter your height')
            else:
                break
        break
    else:
        print('Enter the units of weight and height correctly')
        w_unit = input('Select a unit of weight: kg, lb ')
        h_unit = input('Select a unit of height: ft, cm, in. ')

w = w_float*float(D[w_unit.upper()])
h = h_float*D[h_unit.upper()]

BMI = (w/h**2)*703
print('Your BMI is {:.1f}.'.format(BMI))

if 18.5 <= BMI <= 25:
    print('You are within the ideal weight range')
elif BMI < 18.5:
    print('You are underweight. You should see your doctor.')
elif BMI > 25:
    print('You are overweight. You should see your doctor.')
else:
    print('Your BMI cannot be calculated.')



# import re
#
# w_input = input('Write your weight')
# h_input = input('Write your height')
#
# w_float = float(re.findall('[^a-zA-Z]+', w_input)[0])
# w_unit = re.findall('[a-zA-Z]+',w_input)[0]
#
# h_float = float(re.findall('[^a-zA-Z]+',h_input)[0])
# h_unit = re.findall('[a-zA-Z]+',h_input)[0]
#
# w = w_float*float(D[w_unit.upper()])
# h = h_float*D[h_unit.upper()]
#
# BMI = (w/h**2)*703
# print('Your BMI is {:.1}.'.format(BMI))
#
# if 18.5 <= BMI <= 25:
#     print('You are within the ideal weight range')
# elif BMI < 18.5:
#     print('You are underweight. You should see your doctor.')
# elif BMI > 25:
#     print('You are overweight. You should see your doctor.')
# else:
#     print('Your BMI cannot be calculated.')