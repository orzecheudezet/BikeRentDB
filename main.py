from Bike import *
from BikeRepository import *
import pyodbc


print("Welcome to Bike Rent.")
userChar = ''

while userChar != 'q':
    print("1. Add bike")
    userChar = input("Enter num or q to quit: ")
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
    cursor = cnxn.cursor()

    if userChar == '1':
        bike = Bike(None, None, None, None)
        bike.AddBike()
        bikeRep = BikeRepository(cursor)
        bikeRep.save(bike)
        cnxn.commit()


