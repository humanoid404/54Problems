

#Exercise6-1 & 6-2
import time
birth_year=int(input('when is your birth year?'))
Want=int(input('At what age would you like to retire?'))
current_year=int(time.strftime('%Y', time.localtime(time.time())))
age=current_year-birth_year

left_year= Want-age
if left_year >0:
    print("Your age is %d" %age,
          "You have %d years left until you can retire" %left_year,sep='\n')
    print("It's {0}, so you can retire in {1}".format(current_year,current_year+left_year))
else:
    print('negative number is not permitted')


#Exercise6-1
def Area_of_a_recangular(a, b):
    print('What is the first number? %d' % a)
    print('What is the second number? %d' % b)
    print('You entered dimensions of {0} feet by {1} feet.'.format(a, b))
    m = ((a * b) ** 2) * 0.09290304
    print('The area is {0} square feet i.e {1}'.format(a * b, m))
#Area_of_a_recangular(9,2)