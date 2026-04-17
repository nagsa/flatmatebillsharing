import webbrowser

from fpdf import FPDF


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
