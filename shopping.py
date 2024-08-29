class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price,quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('Total price: ', total)
        if amount < total:
            print(f'please provide {total - amount} taka more')
        else:
            extra = amount - total
            print(f'You get back {extra} taka')

swapan = Shopping('Alan Swapan')
swapan.add_to_cart('alu', 40, 1)
swapan.add_to_cart('dim', 12, 4)
swapan.add_to_cart('rice', 50, 10)

print(swapan.cart)
swapan.checkout(588)