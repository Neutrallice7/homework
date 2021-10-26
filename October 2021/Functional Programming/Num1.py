import math

def convert_to_days():
    hours = float(input('Enter hours: '))
    minutes = float(input('Enter minutes: '))
    seconds = float(input('Enter seconds: '))
    return (hours / 24), ((minutes /60) / 24), (((seconds / 60) / 60) / 24)

x,y,z = convert_to_days()
print('{:.4f}'.format(x + y + z))