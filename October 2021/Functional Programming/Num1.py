import math #imports math

def convert_to_days(): #functions
    hours = float(input('Enter hours: ')) #user inputs
    minutes = float(input('Enter minutes: '))
    seconds = float(input('Enter seconds: '))
    return (hours / 24), ((minutes /60) / 24), (((seconds / 60) / 60) / 24) #conversion to days

x,y,z = convert_to_days()
print('{:.4f}'.format(x + y + z)) #format to 4 significant figures