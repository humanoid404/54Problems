c = 0.09290304
length = 15
width = 20
lenth = float(length)
width = float(width)
area_f = length * width
area_m = area_f * c
[length, width, area_f, area_m] = [str(length), str(width), str(area_f), str(area_m)]
print('What is the length of the room in feet? ', length, '\n',
      'What is the width of the room in feet? ', width, '\n', 'You entered dimensions of ', length, ' feet by ', width, ' feet', '\n',
      'The area is', '\n', area_f, ' square feet', '\n', area_m, ' square meters')