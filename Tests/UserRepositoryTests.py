import pyodbc
from User import *
from UserRepository import *

class UserRepositoryTests:

    @staticmethod
    def Should_Save_User():
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()

        userRep = UserRepository(cursor)
        user = User(93061410930, 'Krzysztof', 'Orzechowski')

        userRep.save(user)

        cnxn.commit()

        cursor.close()
        cnxn.close()

UserRepositoryTests.Should_Save_User()