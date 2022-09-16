import re

class Dialog:

    def getAlphaString(message):
        validString = False
        while not validString:
            string = input(message)
            if string.replace(" ", "").isalpha():
                validString = True
                return string
            else: 
                print("please only enter letters")
    
    def getSalary():
        validSalary = False
        while not validSalary:
            try: 
                salary = int(input("Please enter your annual salary: "))
                if salary >= 5000 and salary <= 2000000:
                    validSalary = True
                    return salary
                else: 
                    print('You must enter a salary between 5 thousand and 2 million')

            except ValueError:
                print('You must enter an integer')

    def getSuper():
        validSuper = False
        while not validSuper:
            try:
                super = int(input("Please enter your super rate: "))
                if super >= 1 and super <= 100:
                    validSuper = True
                    return super
                else: print('You must enter a super rate between 1 and 100')

            except ValueError:
                print('You must enter an integer')
                
    
    def getPaymentDate():
        validDate = False
        while not validDate:
            date = input("Please enter your payment start date: ")
            if re.match("^([0-2][0-9]|(3)[0-1])(\s)(?:(?:Jan|Feb)(?:uary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)", date):
                validDate = True
                return date
            else:
                print("please enter in format (00 Mar)")


