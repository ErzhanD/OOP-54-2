import random

class Heroes:
    def __init__(self, name, hp):
        self.name, self.hp = name, hp

    def action(self): print(f"{self.name} осматривается")
    def attack(self): print(f"{self.name} атакует")

class Archer(Heroes):
    def __init__(self, name, hp, arrows = 10, precision = 0.7):
        super().__init__(name, hp)
        self.arrows, self.precision = arrows, precision

    def attack(self):
        if self.arrows <= 0:
            print(f"{self.name}: нет стрел")
            return
        self.arrows -= 1
        print(f"{self.name}: {'попадание' if random.random() < self.precision else 'промах'}")

    def rest(self):
        self.arrows += 5
        print(f"{self.name}: +5 стрел ({self.arrows})")

    def status(self):
        return f"{self.name}, HP: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision:.2f}"

if __name__ == "__main__":
    test = Archer("Герой", 100)
    print(test.status())
    test.action()
    for _ in range(3): test.attack()
    test.rest()
    print(test.status())