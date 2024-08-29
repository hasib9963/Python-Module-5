# task for me
class Calculator:
    brand = 'Casio MS990'
    def add(self, num1, num2):
        sum = (num1+num2)
        return sum
    
    def subt(self, num1, num2):
        remove = (num1-num2)
        return remove
    
    def mult(self, num1, num2):
        multi = (num1*num2)
        return multi
    
    def div(self, num1, num2):
        division = (num1/num2)
        return division

math = Calculator()

addition = math.add(21, 18)
print(addition)

subtraction = math.subt(21, 18)
print(subtraction)

multiplication = math.mult(21, 18)
print(multiplication)

division = math.div(21, 18)
print(division)

# And i successfully done it, Alhamdulillah.