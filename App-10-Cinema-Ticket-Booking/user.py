from card import Card
from seat import Seat
from ticket import Ticket

class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):

        seat_price = seat.get_price()
        card_validation = card.validate(seat_price,card.cvc)
        seat_availability = seat.is_free()

        if seat.is_free():
            if card.validate(seat_price,card.cvc):
                seat.occupy()
                ticket = Ticket(user=self,price=seat.get_price(),seat_number=seat.seat_id)
                ticket.create_pdf()
                return "You have succesfully submitted your order"
            else:
                return "Sorry, you cannot submit the order, there is a problem with your card"
        else:
            return "Sorry, this seat is already ocuppied"



        # if card_validation  == False:
        #     return "Sorry, you cannot submit the order, there is a problem with your card"
        # elif seat_availability == False:
        #     return "Sorry, this seat is already ocuppied"
        # else:
        #     seat.occupy()
        #     return "You have succesfully submitted your order"