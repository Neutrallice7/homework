class ShopItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = float(amount)
        self.price = self.price_list()
        self.total_price = self.calculate_total()
    def price_list(self):
        if self.name == 'Dry Cured Iberian Ham':
            return 177.80
        elif self.name == 'Wagyu Steaks':
            return 450
        elif self.name == 'Matsutake Mushrooms':
            return 272
        elif self.name == 'Kopi Luwak Coffee':
            return 306.50
        elif self.name == 'Moose Cheese':
            return 487.20
        elif self.name == 'White Truffles':
            return 3600
        elif self.name == 'Blue Fin Tuna':
            return 3603.00
        elif self.name == 'Le Bonnotte Potatoes':
            return 270.81
        else:
            return 0
    def calculate_total(self):
        return self.price * self.amount
    def get_name(self):
        return self.name
    def get_amount(self):
        return self.amount
    def get_price(self):
        return self.price
    def get_total(self):
        return self.total_price