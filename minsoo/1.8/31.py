while 1:
    try:
        resting_HR = int(input('Resting Pulse'))
        age = int(input('Your age'))
        break
    except:
        print('Invalid')
def Target_Heart_Rate(intensity):
    return round((((220 - age) - resting_HR)*intensity) + resting_HR)
print('{:<15}|{:<15}'.format('Intensity', 'Rate'))
print('-'*14, '|', '-'*15)
for i in range(9):
    x = (55+5*i)*0.01
    print(f'{x:.0%}', ' '*11+'|', f'{Target_Heart_Rate(x):3d} bpm')