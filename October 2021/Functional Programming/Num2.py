import math

# weight = mass * gravity 

# try to find the mass in Earth -> use that mass to convert it to Jupiter??

def calc_weight_on_planet(weight=120, gravity=23.1):
    mass = weight / 9.8
    newWeight = mass * gravity
    return newWeight

x = calc_weight_on_planet()
print(x)