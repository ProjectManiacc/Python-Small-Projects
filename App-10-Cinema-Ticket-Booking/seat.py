import sqlite3


class Seat:

    database = 'cinema.db'

    def __init__(self,seat_id):
        self.seat_id = seat_id

    def get_seats_id(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT seat_id FROM Seat 
        """)
        result = cursor.fetchall()

        connection.commit()
        connection.close()

        return result

    def get_price(self,):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT price FROM Seat WHERE seat_id = ?
        """, [self.seat_id])
        result = cursor.fetchall()[0][0]
        connection.close()

        return result

    def get_available(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                SELECT seat_id FROM Seat WHERE taken=0
                """)
        result = cursor.fetchall()
        cursor.commit()
        connection.close()

        return result

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT taken FROM Seat WHERE seat_id=?
                        """,[self.seat_id])
        connection.commit()
        result = cursor.fetchall()[0][0]
        connection.close()
        if result == 0:
            return True
        else:
            return False

    def occupy(self,):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                                UPDATE Seat SET taken=? WHERE seat_id=?
                                """, [1,self.seat_id])
        connection.commit()
        connection.close()
