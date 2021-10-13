import math


Numerator = int(input('Insert your numerator here:'))
while Numerator < 1:
  print('The numerator must be bigger than 0.')
  Numerator = int(input('Insert your numerator here:'))

Denominator = int(input('Insert your denominator here:'))
while Denominator < 0:
  print('The denominator must be bigger than 0.')
  Denominator = int(input('Insert your denominator here:'))


gcd = math.gcd(Numerator, Denominator)

if Numerator<Denominator:
  print('The fractions are proper.')
  if gcd == 1:
    print('The fraction is already reduced. The answer is', Numerator, '/', Denominator)
  else:
    Numerator = Numerator // gcd
    Denominator = Denominator // gcd 
    print('The reduced proper fractions are:', Numerator, '/' ,Denominator )
elif Numerator >= Denominator:
  print('They are improper fractions.')
  if gcd == 1:
    print('The fraction is already reduced. The answer is', Numerator, '/', Denominator)
  else:
    Numerator = Numerator // gcd
    Denominator = Denominator // gcd 
    print('The reduced improper fractions are:', Numerator, '/' , Denominator)
  wNumber = Numerator // Denominator
  remainder = Numerator % Denominator
  if remainder != 0:
      print('The mixed fraction is', wNumber, 'and', remainder, '/', Denominator)
  else:
      print('The whole number is:', wNumber)
