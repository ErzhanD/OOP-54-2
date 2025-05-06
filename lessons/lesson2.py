# # Верблюжоя нотация
# # Змеиная нотация
#
#
# # WarriorHero
# # warrior_hero
#
# # Наследование
#
#
# # Родительский класс - Супер класс
# class Hero:
#
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def interduce(self):
#         return print(f"Я {self.name}, мой уровень {self.lvl}")
#
#     def action(self):
#         return print(f"{self.name} выполняет базовое действие")
#
# hero = Hero("Hero", 100, 100)
#
# # Дочерний класс
# class MageHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def cast_spell(self):
#         return print(f"Кастую огонь")
#
#     def action(self):
#         return print(f"{self.name} ничего не делает")
#
# mage_hero = MageHero("Маг", 100, 100, 1000)
#
# mage_hero.action()
#


# class A:
#
#     def method_a(self):
#         return "A"
#
# class B(A):
#
#     def method_a(self):
#         return "B"
#
# class C(A,B):
#     def method_C(self):
#         return "C"
#
# test = C()
#
#

