import math

# weight = mass * gravity 

# try to find the mass in Earth -> use that mass to convert it to the weight in Jupiter

def calc_weight_on_planet(weight=120, gravity=23.1): #default values
    mass = weight / 9.8 #converts weight to mass in Earth
    newWeight = mass * gravity #converts mass to weight in Jupiter
    return newWeight

x = calc_weight_on_planet() 
print(x) #prints the result