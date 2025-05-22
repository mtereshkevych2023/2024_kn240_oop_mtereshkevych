class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)  # виклик конструктора базового класу
        self.seats = seats

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"

# Використання:
car = Car("Toyota", "Camry", 5)
print(car.display_info())  # Toyota Camry, Seats: 5