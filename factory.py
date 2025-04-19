class Logistics:
    def log(self):
        pass

class SeaLogistics(Logistics):
    def log(self):
        pass
    def create_transport(self):
        return Ship()


class RoadLogistics(Logistics):
    def log(self):
        pass
    def create_transport(self):
        return Truck()


class Transport:
    def go(self):
        pass
class Ship(Transport):
    def go(self):
        print("Ship go")

class Truck(Transport):
    def go(self):
        print("Truck go")




def createtrip():
    name = input("enter your trip type: ")
    if name == "Sea":
        logistics = SeaLogistics()
    if name == "Road":
        logistics = RoadLogistics()


    return logistics.create_transport()


t = createtrip()
t.go()
