import pyodbc
import unittest
from Bike import *
from BikeRepository import *

class BikeRepositoryTest(unittest.TestCase):


    def test_Save_Bike(self):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()

        bikeRep1 = BikeRepository(cursor)
        rower1 = Bike(None, 'red', 28, 'Giant')

        bikeRep1.save(rower1)

        cnxn.commit()

        cursor.close()
        cnxn.close()

