from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        """All child classes must implement this method."""
        pass

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started: Vroom!"
        
    def fuel_type(self):
        return "Petrol"

class ElectricBike(Vehicle):
    def start_engine(self):
        return "Bike powered on: Silent hum."
        
    def fuel_type(self):
        return "Electricity"


my_car = Car()
print(my_car.start_engine())  
print(my_car.fuel_type())    