class Bill:
    """
    Object that contains data about a bill, such as total
    and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays
    a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house


    def pays(self, bill: object, flatmate2: object) -> None:
        weight=(self.days_in_house/(self.days_in_house
                + flatmate2.days_in_house))
        to_pay=bill.amount * weight
        return to_pay

class PdfReport:
    """
    Creates a PDF file that contains data about the
    flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=999, period="March 2026")
john=Flatmate(name="John", days_in_house=20)
marry=Flatmate(name="Mary", days_in_house=25)
print(john.pays(bill=the_bill,flatmate2=marry))
print(marry.pays(bill=the_bill,flatmate2=john))
