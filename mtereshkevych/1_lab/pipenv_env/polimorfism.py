# Приклад ПОЛІМОРФІЗМУ
# Базовий клас
from inheritance import BaseDog, BaseCat, Animal

# Дочірні класи, що реалізують свій варіант методу make_sound()
class Dog(BaseDog):
    # def __init__(self, name):
    #     super().__init__(name)
    
    def make_sound(self):
        return super().make_sound() + " Woof!"

class Cat(BaseCat):
    # def __init__(self, name):
    #     super().__init__(name)
    
    def make_sound(self):
        return super().make_sound() + " Meow!"

class Cow(Animal):
    # def __init__(self, name):
    #     super().__init__(name)
    
    def make_sound(self):
        return "Moo!"
