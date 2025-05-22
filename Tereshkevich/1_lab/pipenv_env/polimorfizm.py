# Базовий клас
class Animal:
    def make_sound(self):
        """Загальний метод, який буде перевизначений у підкласах"""
        pass  # Заглушка, яка змушує дочірні класи реалізувати цей метод

# Дочірні класи, що реалізують свій варіант методу make_sound()
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Функція, яка демонструє поліморфізм
def animal_sound(animal: Animal):
    """Приймає будь-який об'єкт, що наслідує Animal, і викликає make_sound()"""
    print(f"{animal.__class__.__name__} каже: {animal.make_sound()}")

# Демонстрація роботи
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal_sound(animal)