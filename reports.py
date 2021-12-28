from fpdf import FPDF
import webbrowser
import os

#Create a Pdf class that has a generate report method
class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmate such as their names, their due ammount,
    and period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, user, budget):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon to top
        pdf.image(name = "files/icon.png", w=50, h=50,)

        #Insert Title 
        pdf.set_font(family='Times', size = 24, style='B')
        pdf.cell(w=0, h=80, txt=user.user_name+ " 50/30/20 Budget", border=0, align='C', ln=1)

        #Insert Period label and value
        pdf.set_font(family= "Times", size=14, style ='B')
        pdf.cell(w=100, h=40, txt='Period: ' + budget.period, border=0, ln=1)
    

        #Insert Expected Budget Table
        pdf.set_font(family= "Times", size=14, style ='B')
        pdf.cell(w=100, h=40, txt="Expected budget:", border=0, ln=1)
        pdf.set_font(family= "Times", size=12,)
        pdf.cell(w=100, h=40, txt="Needs(50%): "+str(budget.expected_budget(user)[0]), border=0, ln=1)
        pdf.cell(w=100, h=40, txt="Wants(30%): "+str(budget.expected_budget(user)[1]), border=0, ln=1)
        pdf.cell(w=100, h=40, txt="Savings/Debts(20%): "+str(budget.expected_budget(user)[2]),border=0, ln=1)

        #Insert Actual Budget Table
        pdf.set_font(family= "Times", size=14, style ='B')
        pdf.cell(w=100, h=40, txt="Actual budget:", border=0, ln=1)
        pdf.set_font(family= "Times", size=12,)
        pdf.cell(w=100, h=40, txt="Needs(" + str(budget.actual_budget(user)[0])+"): " + str(float(user.needs)), border=0, ln=1)
        pdf.cell(w=100, h=40, txt="Wants(" + str(budget.actual_budget(user)[1])+"): " + str(float(user.wants)), border=0, ln=1)
        pdf.cell(w=100, h=40, txt="Saving(" + str(budget.actual_budget(user)[0])+"): " + str(float(user.savings)), border=0, ln=1)


        #Change directory, Print the Pdf
        os.chdir("files")
        pdf.output(self.filename)

        #Open PDF automaticlly, if windows : webbrowser.open(self.filename)
        webbrowser.open('file://'+os.path.realpath(self.filename))

