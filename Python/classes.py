class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
p = Point(30.0,45.0)
#print(p.x)
#print(p.y)

class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
    
    def addPassenger(self,name):
        if self.openSeats():
            self.passengers.append(name)
            return True
        else:
            return False

    def openSeats(self):
        return self.capacity - len(self.passengers) >0
flight = Flight(3)

people = ["Harry","Ron","Hermione","Draco"]

for i in people:
    success = flight.addPassenger(i)
    print(success)