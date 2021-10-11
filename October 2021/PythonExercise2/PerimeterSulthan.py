x = float(input('Input angle 1:'))
y = float(input('Input angle 2:'))
z = float(input('Input angle 3:'))

Perimeter = x + y + z

if x + y > z and x + z > y and y + z > x:
    print('The perimeter is', Perimeter)
else:
    print('Your input is invalid.')