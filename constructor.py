class Phone:
    manufactured = 'Chaina'
    
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    
    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)

my_phone = Phone('hasib', 'Vivo', 16000)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('she', 'Oppo', 12000)
print(her_phone.owner, her_phone.brand, her_phone.price)
my_phone.send_sms('vivo', 'kemon acen')
her_phone.send_sms('Oppo', 'Onek valo aci')

dad_phone = Phone('Abba', 'Nokia', 1500)
print(dad_phone.owner, dad_phone.brand, dad_phone.price)
dad_phone.send_sms('Nokia', 'Bkash a send korbo')

#HW: pen class, create three object with different instance attribute