from house import Bill, Flatmate
from reports import PdfReport

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


pdfreport= PdfReport(filename=f"{the_bill.period}.pdf")
pdfreport.generate(flatmate1=person1, flatmate2=person2, bill=the_bill)
