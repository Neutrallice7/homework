def convert_temp():
    F = float(input('Insert temperature in Fahrenheit: '))
    C = 5/9 * ( F - 32 )
    K = C + 273.15
    return F,C,K


F,C,K = convert_temp()

print('The temperature in Fahrenheit is', F)
print('The temperature in Celsius is', C)
print('The temperature in Kelvin is', K)
        
