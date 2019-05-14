from UserRepository import *
from BikeRepository import *
from functions import *
import pyodbc


print("Welcome to Bike Rent.")
userChoice = ''

while userChoice != 'q':
    print("1. Add bike")
    print("2. Add user")
    userChoice = input("Enter num or q to quit: ")

    if userChoice == '1':
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()
        bike = createBikeFromInput()
        bikeRep = BikeRepository(cursor)
        bikeRep.save(bike)
        cnxn.commit()
        cursor.close()
        cnxn.close()

    if userChoice == '2':
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()
        user = createUserFromInput()
        userRep = UserRepository(cursor)
        userRep.save(user)
        cnxn.commit()
        cursor.close()
        cnxn.close()

