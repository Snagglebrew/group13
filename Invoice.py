class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for product in products:
            total_impure_price += products[product]['qnt'] * products[product]['unit_price']
        return round(total_impure_price,2)


    def totalDiscount(self, products):
        total_discount = 0
        for product in products:
            total_discount += products[product]['qnt'] * products[product]['unit_price'] * products[product]['discount'] / 100
        self.total_discount = total_discount
        return round(total_discount,2)

    def totalPurePrice(self, products):
        total_pure_price = 0
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return round(total_pure_price,2)
    
    def totalTax(self, products):
        total_tax = 0
        total_tax = self.totalPurePrice(products) * 0.07
        return round(total_tax,2)

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
                break
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput
                break
