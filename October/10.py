class Car:
    def describe(self):
        print("This is a car with four wheels and a comfortable interior.")

class Bike:
    def describe(self):
        print("This is a bike that is lightweight and great for exercise.")

class Truck:
    def describe(self):
        print("This is a truck which is designed for transporting heavy loads")
        
def describe_vehicle(vehicle):
    vehicle.describe()


car = Car()
bike = Bike()
truck = Truck()
describe_vehicle(car) 
describe_vehicle(bike)  
describe_vehicle(truck)
