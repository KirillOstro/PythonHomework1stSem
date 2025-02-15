class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def makesound(self):
        print(f"{self.name} издает звук: {self.sound}")


class Cat(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color


    def makesound(self):
        print(f"{self.name} (цвет: {self.color}) издает звук: {self.sound}")


class Dog(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def makesound(self):
        print(f"{self.name} (цвет: {self.color}) издает звук: {self.sound}")


cat = Cat("Мурзик", "Мяу", "рыжий")
dog = Dog("Шарик", "Гав", "черный")


cat.makesound()
dog.makesound()
