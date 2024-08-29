def call():
    print('Calling someone i don''t know')
    return 'call done'

class Phone:
    price = 12000
    color = 'Natural Titenium'
    brand = "Apple"
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('Calling one person')
    def send_sms(self, phone, sms):
        text = f'sending sms to: {phone} and message: {sms}'
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(41534, 'stop promtional sms')
print(result)