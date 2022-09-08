
class Employee:
    def __init__(self, fname, lname, income, super, paymentS, paymentE):
        self.fname = fname
        self.lname = lname
        self.income = income
        self.super = super
        self.paymentS = paymentS
        self.paymentE = paymentE
    
    def getName(self):
        print(f'Name: {self.fname.capitalize()} {self.lname.capitalize()}')

    def getPayPeriod(self):
        print(f'Pay Period: {self.paymentS} - {self.paymentE}')

    def getGrossIncome(self):
        grossIncome = self.income / 12
        print(f'Gross Income: {round(grossIncome)}')
        return grossIncome

    def getIncomeTax(self):
        i = self.income
        if i <= 18200:
            i = 0
            print(f'Income Tax: {round(i)}') 
        elif i >= 18201 and i <= 37000:
            i = ((i - 18200) * 0.19)/12
            print(f'Income Tax: {round(i)}') 
        elif i >= 37001 and i <= 87000:
            i = (3572 + (i - 37000) * 0.325)/12
            print(f'Income Tax: {round(i)}') 
        elif i >= 87001 and i <= 180000:
            i = (19822 + (i - 87000) * 0.37)/12
            print(f'Income Tax: {round(i)}') 
        elif i >= 180001:
            i = (54232 + (i - 180000) * 0.45)/12
            print(f'Income Tax: {round(i)}') 
        return round(i)

    def getNetIncome(self, gross, tax):
        print(f'Net Income: {round(gross - tax)}')

    def getSuper(self, gross):
        super = self.super / 100
        print(f'Super: {round(gross * super)}')





