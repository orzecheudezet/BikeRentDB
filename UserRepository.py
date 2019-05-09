class UserRepository:
    def __init__(self, cursor):
        self.curosr = cursor


    def save(self, user):
        self.cursor.execute("INSERT INTO Bikes (Color, Size, Brand) VALUES('"+str(user.pesel)+"', '"+user.firstName+"', '"+user.lastName+"')")