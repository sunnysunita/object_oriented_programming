class Vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self.maxSpeed=maxSpeed

class Car(Vehicle):
    def __init__(self,color,maxSpeed,numGear,isConvertable):
        super().__init__(color,maxSpeed)
        self.numGear=numGear
        self.isConvertable=isConvertable

    def print_car_details(self):
        print("car colour: ",self.color)
        print("car maxSpeed: ", self.maxSpeed)
        print("number of gear: ",self.numGear)
        print("is convertable: ",self.isConvertable)

car1=Car("RED",150,6,"YES")
car1.print_car_details()