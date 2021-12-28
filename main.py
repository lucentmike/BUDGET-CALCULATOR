class User:
    """ Creates a user that takes in the name, monthly income,  
    and their the needs, wants, and savings/debts expenses
    """

    def __init__(self, user_name, income):
        self.user_name=user_name
        self.income=income
        
    def needs (self, amount):
        return amount 


    def wants(self, amount):
        return amount 


    def savings(self, amount):
        return amount 



class Budget:
        """ Creates a budget that takes in the budget period,
        and calculates the expected ratios, and actual ratios 
        """

        def __init__(self, period):
            self.period = period


        def expected_budget(self, user1):
            return (user1.income * .50, user1.income * .30, user1.income * .20)


        def actual_budget(self, user1):
             return ("{0:.0%}".format(user1_needs / user1.income), "{0:.0%}".format(user1_wants / user1.income), "{0:.0%}".format(user1_savings / user1.income))



class PdfReport:
        """ Generates a Pdf file that displays user_name, budget period, 
        expected budget, and actual budget
        """

        def __init__ (self, filename ):
            self.filename = filename


        def generate(user_name, budget):
            pass


user1 = User(user_name= 'Kylie', income= 2000)

budget1 = Budget(period = "Jan 2021")

user1_needs = user1.needs(1000)
user1_wants = user1.wants(700)
user1_savings = user1.savings(500)


print ("Expected budget is: Needs(50%):", budget1.expected_budget(user1)[0], ", Wants(30%):", budget1.expected_budget(user1)[1] , ", Savings/Debt(20%):", budget1.expected_budget(user1)[2] )
print (f"Actual Budget is: Needs("+ budget1.actual_budget(user1)[0]+"):", float(user1_needs),", Wants("+ budget1.actual_budget(user1)[1]+"):", float(user1_wants),", Savings/Debts("+ budget1.actual_budget(user1)[2]+"):", float(user1_savings))

