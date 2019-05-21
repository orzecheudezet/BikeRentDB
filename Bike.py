class Bike:
    def __init__(self, id, color, size, brand):
        self.id = id
        self.color = color
        self.size = size
        self.brand = brand

    def __str__(self):
        return ("Object: " + str(self.id) + " " + str(self.color)+ " " + str(self.size) + " " + str(self.brand))



