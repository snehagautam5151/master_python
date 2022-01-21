from abc import ABC

class Car(ABC):
    def mileage(self):
        pass
    
class Honda(Car):
    def mileage(self):
        print ("The mileage is 20 mph")
        
class Chevy(Car):
    def mileage(self):
        print("The mileage is 15 mph")
        
        
