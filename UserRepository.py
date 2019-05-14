class UserRepository:
    def __init__(self, cursor):
        self.cursor = cursor


    def save(self, user):
        self.cursor.execute("INSERT INTO Users (PESEL, FirstName, LastName) VALUES('"+str(user.pesel)+"', '"+user.firstName+"', '"+user.lastName+"')")