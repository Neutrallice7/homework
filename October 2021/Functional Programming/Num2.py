import math

# weight = mass * gravity 

def calc_weight_on_planet(mass=120, gravity=23.1):
    gravity = float(input('Insert gravity here (Leave for default): '))
    return mass, gravity

mass,gravity = calc_weight_on_planet()
print('Your weight is ', mass * gravity)
