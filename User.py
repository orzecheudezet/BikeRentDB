class User:
    def __init__(self, pesel, firstName, lastName):
        self.pesel = pesel
        self.firstName = firstName
        self.lastName = lastName


    def __str__(self):
        return ("Object: " + str(self.pesel) + " " + str(self.firstName) + " " + str(self.lastName))

