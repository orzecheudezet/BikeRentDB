from Bike import *
from User import *

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
    rentPerson = input("Enter PESEL number")
    rentBike = input("Enter bike Id")
    rentDateFrom = input()
