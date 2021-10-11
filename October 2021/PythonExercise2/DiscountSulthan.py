Quantity = float(input('Enter the number of packages that are bought:'))

if Quantity < 10:
    Discount = 0
if 10 <= Quantity <= 19:
    Discount = 10
if 20 <= Quantity <= 49:
    Discount = 20
if 50 <= Quantity <= 99:
    Discount = 30
if Quantity >= 100:
    Discount = 40

Discounted = (99*Quantity) * Discount/100
Total = (99*Quantity) - Discounted

print('Total amount: $', format(Total, '.2f'))
