from budget import User, Budget
from reports import PdfReport

#Takes in user input and executes code

budget1 = Budget(period = input("Enter the budget period (ex: January 2021): "))

user1 = User(user_name= input("Enter your Name: "), income= float(input("Enter your yout total monthly income: ")), \
needs=float(input("Enter your total monthly Needs (Bills, gas, groceries, personal care): ")), \
wants =float(input("Enter your total monthly Wants (Clothing, dining out, gifts: ")), \
savings = float(input("Enter your total monthly Savings/Debts (LT Savins, ST Savings, Credid Cards): ")))

report1=PdfReport(budget1.period)
report1.generate(user1, budget1)