#Creates a user class

class User:
    """
    
     Creates a user that takes in the name, monthly income,  
    and their the needs, wants, and savings/debts expenses
    """

    def __init__(self, user_name, income, needs, wants, savings ):
        self.user_name=user_name
        self.income=income
        self.needs=needs
        self.wants=wants
        self.savings=savings


#Create a Budget class
class Budget:
    """
    
    Creates a budget that takes in the period of the budget,
    then calcuates the expected budget, and actual based on input from user
    """


    def __init__(self, period):
        self.period = period


    def expected_budget(self, user):
        return (user.income * .50, user.income * .30, user.income * .20)


    def actual_budget(self, user):
            return ("{0:.0%}".format(user.needs / user.income), "{0:.0%}".format(user.wants / user.income), "{0:.0%}".format(user.savings / user.income))