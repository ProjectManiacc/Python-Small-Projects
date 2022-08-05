import sqlite3


class Card:
    database = 'banking.db'

    def __init__(self, number, cvc, holder, type):
        self.holder = holder
        self.cvc = cvc
        self.number = number
        self.type = type

    def validate(self, price, cvc):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        	SELECT balance FROM Card WHERE cvc=?
        	""", [cvc])

        result = cursor.fetchall()[0][0]

        if result > price:
            result = result - price
            cursor.execute("""
            UPDATE Card SET balance=? WHERE cvc=?
            """, [result, cvc])
            return True
        else:
            return False
