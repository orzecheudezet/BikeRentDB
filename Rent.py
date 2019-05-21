class Rent:
    def __init__(self, id, person, bike, dateFrom, dateTo, price, status):
        self.id = id
        self.person = person
        self.bike = bike
        self.dateFrom = dateFrom
        self.dateTo = dateTo
        self.price = price
        self.status = status

    def __str__(self):
        return ("Object: " + str(self.id) + " " + str(self.person) + " " + str(self.bike)
                + " " + str(self.dateFrom) + " " + str(self.dateTo) + " " + str(self.price) + " " + str(self.status))

