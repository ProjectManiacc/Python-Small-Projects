import random
import string

from fpdf import FPDF


class Ticket:

    def __init__(self,user,price, seat_number):
        self.seat_number = seat_number
        self.price = price
        self.user = user
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])

    def create_pdf(self):
        pdf = FPDF(orientation='P',unit='pt',format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1,ln=1,align="C")

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100,h=25,txt='Name: ',border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0,h=25,txt=self.user.name,border=1,ln=1)
        pdf.cell(w=0,h=5,txt='',border=0,ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='TicketID: ', border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt='', border=0, ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Price: ', border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt='', border=0, ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Seat Number: ', border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt='', border=0, ln=1)

        pdf.output("ticket.pdf", 'F')
