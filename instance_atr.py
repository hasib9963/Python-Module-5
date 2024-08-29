class Shop:
    Shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = Shop('Mehjabeen')
mehjabeen.add_to_cart('Shoes')
mehjabeen.add_to_cart('Smartphone')
print(mehjabeen.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('Cap')
nisho.add_to_cart('Watch')
print(nisho.cart) 

apurba = Shop("Apurbo")
apurba.add_to_cart('T-Shirt')
apurba.add_to_cart('Punjabi')
print(apurba.cart)