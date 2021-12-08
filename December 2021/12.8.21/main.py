from shop_item import ShopItem

cart = []

# checks for validation
while True:
    user_items = int(input('How many items will you order today? '))
    
    if user_items < 1:
        print('Number must be at least 1.')
    else:
        break
# repeats the print
for i in range(user_items):
    print('Item #'+str(i+1))
    food_name = input('Enter food:')
    # validation check
    while True:
        amount_pound = float(input('Enter amount of pounds: '))

        if amount_pound <= 0:
            print('Amount of pounds must be greater than 0.')
        else: 
            break

    print()
    cart.append(ShopItem(food_name, amount_pound))

print('Here\'s a summary of the items purchased:')
print('----------------------------------------------')
#prints out every order
for checkout in cart:
    print('Item: '+checkout.get_name())
    print('Amount ordered: '+str(checkout.get_amount()))
    print('Pricer per pound: '+str(checkout.get_price()))
    print('Price of order: '+str(checkout.calculate_total()))
#adds everything
total = 0
for checkout in cart:
    total += checkout.get_total()

print('Total cost: '+str(total))
    


