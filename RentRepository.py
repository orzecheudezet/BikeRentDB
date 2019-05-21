from Rent import *

class RentRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def save(self, rent):
        self.cursor.execute("INSERT INTO Rents (Person, Bike, DateFrom, DateTo, Price, Status) VALUES"
                            "('"+str(rent.person)+"', '"+str(rent.bike)+"', '"+str(rent.dateFrom)+"', "
                            "'"+str(rent.dateTo)+"', '"+str(rent.price)+"', '"+str(rent.status)+"' )")


    def load(self, idRent):
        self.cursor.execute("SELECT * FROM Rents WHERE Id = '"+str(idRent)+"'")
        record = self.cursor.fetchall()
        for row in record:
            id = row[0]
            person = row[1]
            bike = row[2]
            dateFrom = row[3]
            dateTo = row[4]
            price = row[5]
            status = row[6]
        rent = Rent(id, person, bike, dateFrom, dateTo, price, status)
        return rent

    def update(self, rent):
        rent.status = 1
        self.cursor.execute("UPDATE Rents SET Status = '"+str(rent.status)+"' WHERE Id = '"+str(rent.id)+"'")






