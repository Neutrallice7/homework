def convert_temp(): 
    F = float(input('Insert temperature in Fahrenheit: ')) #user input
    C = 5/9 * ( F - 32 ) #formulas to convert
    K = C + 273.15
    return F,C,K


F,C,K = convert_temp() #functions

print('The temperature in Fahrenheit is', F) #prints output
print('The temperature in Celsius is', C)
print('The temperature in Kelvin is', K)
        
