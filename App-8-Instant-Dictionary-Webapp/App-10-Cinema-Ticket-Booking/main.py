from user import User
from card import Card
from seat import Seat
from ticket import Ticket
import sqlite3

if __name__ == '__main__':
    user = User('John')
    seat = Seat("B2")
    card = Card('12345678','123',user,'Visa')
    print(user.buy(seat,card))




