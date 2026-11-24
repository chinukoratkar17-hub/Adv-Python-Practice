# Factory Design Pattern

class Car:
    def drive(self):
        print("Car is driving")

class Bike:
    def drive(self):
        print("Bike is driving")

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            return None

vehicle = VehicleFactory.get_vehicle("car")
if vehicle:
    vehicle.drive()
