'''Exercise 31 <Karvonen Heart Rate>'''

#1. General

#Karvonen Heart Rate formula
def THR(age,restingHR,intensity):
    THR=(((220-age)-restingHR)*intensity)+restingHR
    return THR

import pandas as pd
age=22
restingHR=65

THR_l = []
intensity=0.50
while intensity<0.95:
    intensity+=0.05
    intensity_p=str(round(intensity*100))+'%'
    THR_p=str(round(THR(age,restingHR,intensity)))+' bpm'
    THR_l.append([intensity_p,THR_p])

#setting for table
columns=['Intensity','Rate']
print(f"Resting Pulse: {restingHR}  Age: {age}")
print(pd.DataFrame(THR_l,columns=columns))


