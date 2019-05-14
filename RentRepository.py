class RentRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def save(self, rent):
        self.cursor.execute("INSERT INTO Rents (Person, Bike, DateFrom, DateTo, Price, Status) VALUES"
                            "('"+str(rent.Person)+"', '"+str(rent.Bike)+"', '"+str(rent.dateFrom)+"', "
                            "'"+str(rent.dateTo)+"', '"+str(rent.price)+"', '"+str(rent.status)+"' )")