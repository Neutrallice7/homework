import math

Force = float(input('Input the amount of force in Newton: '))
Mass = float(input('Input the amount of mass you want to add in Kilos: '))
Gravity = 9.8

Angle = math.asin(Force/(Mass*Gravity))
Degrees = format(math.degrees(Angle), '.1f')

print('The angle of the ramp is', Degrees)