class User:
    def __init__(self, firstName, lastName, pesel):
        self.firstName = firstName
        self.lastName = lastName
        self.pesel = pesel

    def __str__(self):
        return ("Object: " + str(self.firstName) + " " + str(self.lastName) + " " + str(self.pesel))

