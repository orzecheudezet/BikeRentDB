from Bike import *
from BikeRepository import *
from functions import *
import pyodbc


print("Welcome to Bike Rent.")
userChoice = ''

while userChoice != 'q':
    print("1. Add bike")
    print("2. Add user")
    userChoice = input("Enter num or q to quit: ")
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
    cursor = cnxn.cursor()

    if userChoice == '1':
        bike = createBikeFromInput()
        bikeRep = BikeRepository(cursor)
        bikeRep.save(bike)
        cnxn.commit()

    #if userChoice == '2':





