class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой age {self.age}, мой city {self.city}")

    def is_adult(self):
        return self.age >= 18

person1 = Person("Темирлан", 18, "Бишкек")
person1.introduce()

person1 = Person("Темирлан", 18, "Бишкек")
person2 = Person("Самат", 18, "Бишкек")
person3 = Person("Атай", 18, "Бишкек")
person4 = Person("Ришат", 18, "Бишкек")

print(person1.name, "старше или равен 18-ти?", person1.is_adult())
print(person2.name, "старше или равен 18-ти?", person2.is_adult())
print(person3.name, "старше или равен 18-ти?", person3.is_adult())
print(person4.name, "старше или равен 18-ти?", person4.is_adult())