from bank import BankAccount
from inheritance import *
from abstraction import *
from polimorfism import *

if __name__ == "__main__":
    # Демонстрація роботи
    account = BankAccount("Богдан", 1000)
    print(account.owner)  # Публічний атрибут доступний
    # print(account.__balance)  # Викличе помилку, бо атрибут приватний

    account.deposit(500)
    account.withdraw(300)
    print("Поточний баланс:", account.get_balance)

    # Примусове звернення до приватного атрибута (небажано)
    print("Прямий доступ:", account._BankAccount__balance)  # Можливий, але не рекомендований підхід
    # Демонстрація наслідування
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(f"{dog.name} каже: {dog.make_sound()}, {dog.type}")  # Виведе: Buddy каже: Woof! Woof!
    print(f"{cat.name} каже: {cat.make_sound()}, {cat.hight}")  # Виведе: Whiskers каже: Meow!

    # Демонстрація роботи
    vehicles = [Car("Tesla"), Boat("Yamaha"), Airplane("Boeing")]

    for vehicle in vehicles:
        print(vehicle.move())
    
    # Функція, яка демонструє поліморфізм
    def animal_sound(animal: Animal):
        """Приймає будь-який об'єкт, що наслідує Animal, і викликає make_sound()"""
        print(f"{animal.__class__.__name__} каже: {animal.make_sound()}")

    # Демонстрація роботи
    animals = [Dog("Шарік"), Cat("Мурзик"), Cow("Корівка")]

    for animal in animals:
        animal_sound(animal)