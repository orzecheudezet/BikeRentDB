from Bike import *
from User import *
from Rent import *

def createBikeFromInput():
    bikeId = None
    bikeColor = input("Enter color: ")
    bikeSize = input("Enter size: ")
    bikeBrand = input("Enter brand: ")

    bike = Bike(bikeId, bikeColor, bikeSize, bikeBrand)
    return bike

def createUserFromInput():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    pesel = input("Enter PESEL number: ")

    user = User(pesel, firstName, lastName)
    return user

def createRentFromNput():
    rentId = None
    rentPerson = input("Enter PESEL number: ")
    rentBike = input("Enter bike Id: ")
    rentDateFrom = input("Enter rent date YYYY-MM-DD: ")
    rentDateTo = input("Enter return date YYYY-MM-DD: ")
    rentPrice = input("Enter price: ")
    rentStatus = 0

    rent = Rent(rentId, rentPerson, rentBike, rentDateFrom, rentDateTo, rentPrice, rentStatus)
    return rent