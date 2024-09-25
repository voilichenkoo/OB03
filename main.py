# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и
# методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса
# `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук
# для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические
# методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#  Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.



class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(" Подает голос")

    def eat(self):
        print(f"{self.name} кушает")

class Bird(Animal):

    def make_sound(self):
        print(f"{self.name} поет")

    def eat(self):
        print("Питается насекомыми")

class Mammal(Animal):

    def make_sound(self):
        print(f"{self.name} рычит")

    def eat(self):
        print("Питается молоком матери")

class Reptile(Animal):

    def make_sound(self):
        print(f"{self.name} шипит")

    def eat(self):
        print("Питается мясом")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} - {self.position}"


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Animal {animal.name} added to the zoo.")
        else:
            print("Invalid animal.")

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"Employee {employee.name} added to the zoo.")
        else:
            print("Invalid employee.")

    def show_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(f"{animal.name} - {animal.__class__.__name__}")

    def show_employees(self):
        print("Employees in the zoo:")
        for employee in self.employees:
            print(employee)



def animal_sound(animal):
    animal.make_sound()


zoo = Zoo()

lion = Mammal("Лион", 5)
tiger = Mammal("Амур", 3)
parrot = Bird( "Гоша", 2)
snake = Reptile("Маруся", 30)


zoo.add_animal(lion)
zoo.add_animal(tiger)
zoo.add_animal(parrot)
zoo.add_animal(snake)

# Добавление сотрудников
employee1 = Employee("Иван", "Zookeeper")
employee2 = Employee("Алиса Сергеевна", "Veterinarian")

zoo.add_employee(employee1)
zoo.add_employee(employee2)

# Отображение информации о животных и сотрудниках
zoo.show_animals()
zoo.show_employees()

for animal in zoo.animals:
    animal_sound(animal)

