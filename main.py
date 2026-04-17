import webbrowser

from fpdf import FPDF

from house import Bill, Flatmate


class PdfReport:
    """
    Creates a PDF file that contains data about the
    flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay=str(round(flatmate1.pays(bill,flatmate2),2))
        flatmate2_pay=str(round(flatmate2.pays(bill,flatmate1),2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # insert icon

        pdf.image("house.png", w=30, h=30)
        # Insert title of PDF

        pdf.set_font('Arial', 'B', size=24)
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1)

        # Insert period lable and value
        pdf.set_font('Arial', 'B', size=16)
        pdf.cell(w=100, h=40, txt='Period :', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert flatmate 1 name and sharing amount
        pdf.set_font('Arial', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert flatmate 2 name and sharing amount

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)


        pdf.output(self.filename)

        webbrowser.open(self.filename)

input_billamt=float(input("Greetings, Please Enter Total Bill Amount : "))
input_billperiod=input("Please Enter Bill Period in Month YYYY format : ")
input_flatmate1=input("Please Enter First Flatmate Name : ")
input_flatmat1day=int(input(f"How many days {input_flatmate1} stayed in house during bill period? "))
input_flatmate2=input("Please Enter Second Flatmate Name : ")
input_flatmat2day=int(input(f"How many days {input_flatmate2} stayed in house during bill period? "))

the_bill = Bill(amount=input_billamt, period=input_billperiod)
person1= Flatmate(name=input_flatmate1, days_in_house=input_flatmat1day)
person2= Flatmate(name=input_flatmate2, days_in_house=input_flatmat2day)
print(f"{input_flatmate1} pays : ",person1.pays(bill=the_bill,flatmate2=person2))
print(f"{input_flatmate2} pays : ",person2.pays(bill=the_bill,flatmate2=person1))


pdfreport=PdfReport(filename=f"{the_bill.period}.pdf")
pdfreport.generate(flatmate1=person1, flatmate2=person2, bill=the_bill)
