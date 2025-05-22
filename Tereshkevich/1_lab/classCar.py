class Car:
    def __init__(self, make, model, fuel_level=0):
        self.make = make 
        self.model = model
        self.__fuel_level = fuel_level 
        self.__max_fuel = 50  

    def refuel(self, amount):
        if amount <= 0:
            return "Amount to refuel must be greater than zero."
        if self.__fuel_level + amount > self.__max_fuel:
            self.__fuel_level = self.__max_fuel
            return "Tank is full!"
        self.__fuel_level += amount
        return f"Refueled by {amount} liters. Current fuel level: {self.__fuel_level} liters."

    def drive(self, distance):
      
        fuel_needed = distance * 0.1 
        if fuel_needed > self.__fuel_level:
            return "Not enough fuel to drive."
        self.__fuel_level -= fuel_needed
        return f"Drove {distance} km. Remaining fuel: {self.__fuel_level} liters."

    def get_fuel_level(self):
        return self.__fuel_level


car = Car("Toyota", "Corolla", 10)  
print(car.refuel(30))
print(car.drive(50)) 
print(car.get_fuel_level()) 
