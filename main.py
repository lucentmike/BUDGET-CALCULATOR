#Import classes 

from budget import User, Budget
from reports import PdfReport

#Takes in user input and executes code

budget = Budget(period = input("Enter the budget period (ex: January 2021): "))

while True:

    try:
        user = User(user_name= input("Enter your Name: "), income= float(input("Enter your yout total monthly income: ")), \
        needs=float(input("Enter your total monthly Needs (Bills, Gas, Groceries, Personal Care): ")), \
        wants =float(input("Enter your total monthly Wants (Clothing, Dining Out, Gifts: ")), \
        savings = float(input("Enter your total monthly Savings/Debts (LT Savins, ST Savings, Credit Cards): ")))
        break
    except:
       print("That is not a valid entry!")

report=PdfReport(budget.period)
report.generate(user, budget)