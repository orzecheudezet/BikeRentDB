import pyodbc
import unittest
from User import *
from UserRepository import *

class UserRepositoryTests(unittest.TestCase):


    def test_Save_User(self):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()

        userRep = UserRepository(cursor)
        user = User(93061410930, 'Krzysztof', 'Orzechowski')

        userRep.save(user)

        cnxn.commit()

        cursor.close()
        cnxn.close()

