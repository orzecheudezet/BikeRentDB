from UserRepository import *
from BikeRepository import *
from RentRepository import *
from functions import *
import pyodbc


print("Welcome to Bike Rent.")
userChoice = ''

while userChoice != 'q':
    print("1. Add bike")
    print("2. Add user")
    print("3. Rent a bike")
    print("4. Return bike")
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

    if userChoice == '3':
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()
        rent = createRentFromNput()
        rentRep = RentRepository(cursor)
        rentRep.save(rent)
        cnxn.commit()
        cursor.close()
        cnxn.close()

    if userChoice == '4':
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
        cursor = cnxn.cursor()
        rentId = input("Enter rent id: ")
        rentRep = RentRepository(cursor)
        rent = rentRep.load(rentId)
        rentRep.update(rent)
        cnxn.commit()
        cursor.close()
        cnxn.close()




