# Инкапсуляция
#
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = None
#         self.set_grade(grade)
#
#     def set_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.grade = grade
#         else:
#             print("Оценка должна быть от 0 до 100")
#
#     def get_grade(self):
#         return self.grade
#
#     def get_info(self):
#         return f"Имя: {self.name}, Оценка: {self.grade}"
#
# student = Student("Иван", 85)
# print(student.get_info())
#


# Абстракция

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

circle = Circle(5)
square = Square(4)

print(f"Площадь круга: {circle.area()}")
print(f"Площадь квадрата: {square.area()}")