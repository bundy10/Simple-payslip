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
            salary = input("Please enter your annual salary: ")
            if salary.isdigit():
                validSalary = True
                return int(salary)
            else: 
                print('you must enter an integer')

    def getSuper():
        validSuper = False
        while not validSuper:
            super = int(input("Please enter your super rate: "))
            if super >= 1 and super <= 100:
                validSuper = True
                return super
            else: print('You must enter a super rate between 1 and 100')

                
    
    def getPaymentDate():
        validDate = False
        while not validDate:
            date = input("Please enter your payment start date: ")
            if re.match("^([0-2][0-9]|(3)[0-1])(\s)(?:(?:Jan|Feb)(?:uary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)", date):
                validDate = True
                return date
            else:
                print("please enter in format (00 Mar)")


