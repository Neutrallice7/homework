import math

x = float(input('Input your number of Fahrenheit:'))
y = float(input('Input your wind speed:'))

while not -58 < x < 41:
    print('Temperature must be between -58F and 41F')
    x = float(input('Input your number of Fahrenheit:'))
while not y >= 2:
    print('Speed must be greater than or equal to 2')
    y = float(input('Input your wind speed:'))

answer = 35.74 + (0.6215*x) - 35.75*math.pow(y, 0.16) + 0.4275*x*math.pow(y, 0.16)

print('The answer is', format(answer, '.3f'))
