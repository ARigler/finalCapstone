"""
Pseudocode:

START
    ASSIGN False TO VARIABLE "valid_input"
    WHILE NOT valid_input
        PRINT "Choose either 'investment' or 'bond' from the menu below to proceed: \n"
        PRINT "investment   -   to calculate the amount of interest you'll earn on your investment"
        PRINT "bond         -   to calculate the amount you'll have to pay on a home loan"
        GET INPUT
        ASSIGN INPUT TO VARIABLE "calculation_mode"
        calculation_mode = calculation_mode.lower()
        IF calculation_mode == "investment"
            valid_input = True
            ASSIGN False TO "investment_valid_input"
            PRINT "How much money are you depositing?"
            GET INPUT
            ASSIGN INPUT TO VARIABLE "investment_deposit"
            CAST investment_deposit TO TYPE FLOAT
            PRINT "What percentage is the interest rate?"
            GET INPUT
            ASSIGN INPUT TO VARIABLE "investment_rate"
            CAST investment_rate TO TYPE FLOAT
            PRINT "How many years will you invest?"
            GET INPUT
            ASSIGN INPUT TO VARIABLE "investment_years"
            CAST investment_years TO TYPE INTEGER, FLOAT
            WHILE NOT investment_valid_input
                PRINT "Do you want simple or compound interest?"
                GET INPUT
                ASSIGN INPUT TO VARIABLE "interest"
                interest = interest.lower()
                IF interest == "simple"
                    investment_valid_input = true
                    ASSIGN investment_deposit*(1+(investment_rate*investment_years/100.0)) TO VARIABLE "total"
                ELIF interest == "compound"
                    investment_valid_input = true
                    ASSIGN investment_deposit*math.pow(1+(investment_rate/100.0),investment_years) TO VARIABLE "total"
                ELSE
                    PRINT "That was not a valid input, try again."
            PRINT "Your total is R"+total+"."
        ELIF calculation_mode == "bond"
            valid_input = True
            PRINT "Input the present value of the house."
            GET INPUT
            ASSIGN INPUT TO VARIABLE "bond_present"
            CAST bond_present TO TYPE FLOAT
            PRINT "Input the interest rate percentage"
            GET INPUT
            ASSIGN INPUT TO VARIABLE "bond_rate"
            CAST bond_rate TO TYPE FLOAT
            PRINT "Input the number of months you plan to take to repay the bond"
            GET INPUT
            ASSIGN INPUT TO VARIABLE "bond_months"
            CAST bond_months TO TYPE INT, FLOAT
            ASSIGN (bond_rate*bond_present/12.0)/(1-math.pow(1+(bond_rate/12),-bond_months)) TO VARIABLE "repayment_monthly"
            PRINT "You will have to pay back R"+repayment_monthly+" a month."
        ELSE
            PRINT "That was not a valid input, try again"
END
"""
import math #for math.pow()

valid_input = False #set up calculation_mode validation flag
while not valid_input: #start of outer validation loop
    #get the mode string from the user and lowercase it.
    #I know it's a long line, but it's the most efficient way to lay it out
    calculation_mode = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n investment   -   to calculate the amount of interest you'll earn on your investment \n bond         -   to calculate the amount you'll have to pay on a home loan \n").lower()
    if calculation_mode == "investment": #user picks investment
        valid_input = True #set validation flag
        investment_valid_input = False #set up validation flag for interest type
        #Best practice any time you have the user enter information you're parsing into a data type to wrap it in a try-except clause
        #To catch Value Errors, but it seems out of the scope of this task.
        investment_deposit = float(input("How much money are you depositing?\n"))
        investment_rate = float(input("What percentage is the interest rate?\n"))/100.0 #divide interest rate by 100 because it's a percentage and we want decimal value.
        #We also don't have to deal with % sign input
        investment_years = float(int(input("How many years will you invest?\n"))) #we're not allowing fractional years so cast it to int to get rid of floating point, then cast it to float for type convenience
        while not investment_valid_input: #determine interest type
            interest = input("Do you want simple or compound interest?\n").lower()
            if interest == "simple":
                investment_valid_input = True #set validation flag
                #calculate total
                total = investment_deposit*(1+(investment_rate*investment_years))
            elif interest == "compound":
                investment_valid_input = True
                #calculate total
                total = investment_deposit*math.pow((1+investment_rate),investment_years)
            else:
                print("That was not a valid input, try again.")
        print(f"Your total comes to R{total:.2f}.")
    elif calculation_mode == "bond": #user picks bond
        valid_input = True #set validation flag
        bond_present = float(input("Input the present value of the house. \n"))
        bond_rate = float(input("Input the interest rate percentage.\n"))/(100.0*12.0) #divide by 100 because it's a percentage, and divide by 12 because it's monthly and not annual.
        bond_months = float(int(input("Input the number of months you plan to take repaying.\n"))) #we're not allowing fractional months so cast it to int to get rid of floating point, then cast it to float for type convenience
        repayment_monthly = (bond_rate*bond_present)/(1-math.pow(1+bond_rate,-bond_months))
        print(f"Based on the data you've entered, you will have to pay R{repayment_monthly:.2f} a month.")
    else:
        print("That was not a valid answer, try again.")