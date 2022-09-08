from employee import Employee

def main():
    print("Welcome to the payslip generator!")

    fname = input("\nPlease input your name: ")
    lname = input("Please input your surname: ")
    income = int(input("Please enter your annual salary: "))
    super = int(input("Please enter your super rate: "))
    paymentS = input("Please enter your payment start date: ")
    paymentE = input("Please enter your payment end date: ")

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
