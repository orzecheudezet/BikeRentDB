import pyodbc
import unittest
from RentRepository import *
from Rent import *

class RentRepositoryTests(unittest.TestCase):

    def test_Save_Rent(self):
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()

        rentRep = RentRepository(cursor)
        rent = Rent(None, 93061410930, 17, '2019-05-16', '2019-05-20', 20, 0)

        rentRep.save(rent)

        cnxn.commit()


    def test_Load_Rent(self, id):
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()

        rep1 = RentRepository(cursor)
        rent = rep1.load(id)
        print(rent)


