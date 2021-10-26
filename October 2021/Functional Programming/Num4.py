# z is less than m

# formula = (height / width) * New Width 

def calc_new_height():
    while True:
        x = float(input('Insert x here: '))
        y = float(input('Insert y here: '))
        z = float(input('Insert z here: '))
        if z > x:
            continue
        else:
            break
    newHeight = (y / x) * z
    return newHeight

LULE = calc_new_height()
print(LULE)

