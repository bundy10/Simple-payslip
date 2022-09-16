from employee import Employee
from dialog import Dialog

def main():
    print("Welcome to the payslip generator!")

    fname = Dialog.getAlphaString("Please input your name: ")
    lname = Dialog.getAlphaString("Please input your surname: ")
    income = Dialog.getSalary()
    super = Dialog.getSuper()
    paymentS = Dialog.getPaymentDate()
    paymentE = Dialog.getPaymentDate()

    bundy = Employee(fname, lname, income, super, paymentS, paymentE)
    print("\nYour payslip has been generated:\n")
    bundy.getName()
    bundy.getPayPeriod()
    grossIncome = bundy.getGrossIncome()
    incomeT = bundy.getIncomeTax()
    bundy.getNetIncome(grossIncome, incomeT)
    bundy.getSuper(grossIncome)
    
    

    print("\nThank you for using MYOB!")


main()
