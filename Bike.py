class Bike:
    def __init__(self, id, color, size, brand):
        self.id = id
        self.color = color
        self.size = size
        self.brand = brand

    def __str__(self):
        return ("Object: " + str(self.id) + " " + str(self.color)+ " " + str(self.size) + " " + str(self.brand))

    def AddBike(self):
        self.id = None
        self.color = input("Enter color: ")
        self.size = input("Enter size: ")
        self.brand = input("Enter brand: ")
