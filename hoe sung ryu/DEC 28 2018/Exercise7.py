def Area_of_a_recangular(a, b):
    print('What is the first number? %d' % a)
    print('What is the second number? %d' % b)
    print('You entered dimensions of {0} feet by {1} feet.'.format(a, b))
    m = ((a * b) ** 2) * 0.09290304
    print('The area is {0} square feet i.e {1}'.format(a * b, m))

Area_of_a_recangular(9,2)
