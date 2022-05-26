from abc import ABC 
#this line is important to use abstract classes in python
#abstract classes do not have definitions of their own the classes inheriting those put their own implementations
#ABC stands for abstract base class

class Vehicle(ABC): #inherits from abstract class ABC
    def noofwheels(self):
        pass
class Bike(Vehicle):
    def noofwheels(self):
        print("The bike has 2 wheels")
class Car(Vehicle):
    def noofwheels(self):
        print("The car has 3 wheels")
class Truck(Vehicle):
    def noofwheels(self):
        print("The truck has 4 wheels")
bike=Bike()
bike.noofwheels()
car=Car()
car.noofwheels()
truck=Truck()
truck.noofwheels()
