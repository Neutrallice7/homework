Quantity = float(input('Enter the number of packages that are bought:'))

if Quantity < 10:
    Discount = 0
elif 10 <= Quantity <= 19:
    Discount = 10
elif 20 <= Quantity <= 49:
    Discount = 20
elif 50 <= Quantity <= 99:
    Discount = 30
else:
    Discount = 40

Discounted = (99*Quantity) * Discount/100
Total = (99*Quantity) - Discounted

print('Total amount: $', format(Total, '.2f'))